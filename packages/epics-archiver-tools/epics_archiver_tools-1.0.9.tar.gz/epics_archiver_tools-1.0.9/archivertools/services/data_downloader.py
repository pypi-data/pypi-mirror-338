from urllib3 import PoolManager, disable_warnings
disable_warnings()
from datetime import datetime
from typing import List
from ..pv import PV
import os
import json
import warnings
import numpy as np
import pandas as pd
from urllib.parse import urlparse
import pytz


class DataDownloader:
    """Manages data download and interaction with the EPICS archiver server.

    This class handles all communication with the EPICS archiver server, including
    data retrieval, property fetching, and connection verification.

    Attributes:
        __ARCHIVER_URL (str): Base URL of the archiver server.
        __DATA_JSON (str): URL path for retrieving JSON data.
        __CHANNEL_FINDER (str): URL path for retrieving PV properties.
        __epics_timezone (pytz.timezone): Timezone of the EPICS archiver server.

    Note:
        The class automatically verifies server connectivity on initialization
        unless explicitly disabled.
    """
    
    def __init__(self, archiver_url: str = None, check_connection: bool = True):
        """Initialize the DataDownloader with server configuration.

        Args:
            archiver_url (str, optional): The URL of the archiver server. If None,
                defaults to 'http://localhost:17665'.
            check_connection (bool, optional): If True, verifies server connectivity
                on initialization. Defaults to True.

        Raises:
            ConnectionError: If check_connection is True and the server is unreachable.
        """
        self.__ARCHIVER_URL: str = archiver_url or 'http://localhost:17665'
        self.__DATA_JSON: str = '/archappl_retrieve/data/getData.json?'
        self.__CHANNEL_FINDER: str = '/ChannelFinder/resources/channels?'
        self.__http = PoolManager()

        if check_connection:
            is_reachable = self.__ping_archiver()
            if is_reachable is False:
                raise ConnectionError("Archiver server is unreachable. Please check your connection and server URL.")
            print('Archiver server is reachable via ping.')

    def __ping_archiver(self) -> bool:
        """Verify if the archiver server is reachable via ping.

        Returns:
            bool: True if the server is reachable, False otherwise.

        Note:
            This method uses the system's ping command to verify connectivity.
            The hostname is extracted from the archiver URL for the ping test.
        """
        sep = '=' * os.get_terminal_size().columns
        print(sep)
        print("Verifying the reachability of the archiver's server...")
        hostname = urlparse(self.__ARCHIVER_URL).netloc
        if not hostname:
            hostname = self.__ARCHIVER_URL
        exit_status: int = os.system(f"ping -c 1 {hostname}")
        print(sep)
        return exit_status == 0

    def __http_request(self, url: str) -> List:
        """Perform an HTTP request to the archiver server.

        Args:
            url (str): The complete URL for the request.

        Returns:
            List: The JSON response data from the server.

        Note:
            This method uses urllib3's PoolManager with certificate verification
            disabled for the HTTP request.
        """
        http: PoolManager = PoolManager(cert_reqs='CERT_NONE')
        response = http.request('GET', url)
        data: bytes = response.data
        json_data: list = json.loads(data)        
        return json_data

    def __download_data(self, pv_name: str, 
                       start: datetime, 
                       end: datetime,
                       verbose: bool = False) -> pd.DataFrame:
        """Download raw data from the archiver for a specific PV.

        Args:
            pv_name (str): Name of the Process Variable to download.
            start (datetime): Start time for data retrieval in EPICS timezone.
            end (datetime): End time for data retrieval in EPICS timezone.
            verbose (bool, optional): If True, prints progress information.
                Defaults to False.

        Returns:
            pd.DataFrame: Raw data downloaded from the archiver.

        Note:
            The timestamps are automatically converted to UTC for the request.
        """
        if verbose: print(f"Downloading data from {start} to {end}")
        
        # Convert to UTC for the request
        start_utc = start.astimezone(pytz.UTC)
        end_utc = end.astimezone(pytz.UTC)

        url_components: list = [
            self.__ARCHIVER_URL,
            self.__DATA_JSON,
            f'pv={pv_name}&',
            f'from={start_utc.isoformat()}Z&'
            f'to={end_utc.isoformat()}Z&',
            'fetchLatestMetadata=true',
        ]
        url: str = "".join(url_components)
        
        data: dict = self.__http_request(url)[0]

        data_keys: list = list(data['data'][0].keys())
        if 'fields' in data_keys: 
            data_keys.remove('fields')
        df: pd.DataFrame = pd.DataFrame({k: np.array([d[k] for d in data['data']]) for k in data_keys})
                
        return df
    
    def __filter_data(self, df: pd.DataFrame, start_ts: int, end_ts: int) -> pd.DataFrame:
        """Filter data within a specified timestamp range.

        Args:
            df (pd.DataFrame): PV data to filter.
            start_ts (int): Start timestamp in seconds since epoch.
            end_ts (int): End timestamp in seconds since epoch.

        Returns:
            pd.DataFrame: Filtered data containing only records within the specified range.

        Note:
            If exact timestamps are not found, the method adds records with the
            requested timestamps using the last valid values before those times.
        """
        if start_ts not in df['secs'].values:
            record: pd.DataFrame = df[df['secs'] < start_ts].tail(1)
            record['secs'] = start_ts
            idx: int = int(record.index[0]) + 1
            df = pd.concat([df.iloc[:idx], record, df.iloc[idx:]]).reset_index(drop=True)
        if end_ts not in df['secs'].values:
            record: pd.DataFrame = df[df['secs'] < end_ts].tail(1)
            record['secs'] = end_ts
            idx: int = (record.index[0]) + 1
            df = pd.concat([df.iloc[:idx], record, df.iloc[idx:]]).reset_index(drop=True)
        left_mask: pd.Series = df['secs'] >= start_ts
        right_mask: pd.Series = df['secs'] <= end_ts
        df = df.loc[left_mask & right_mask, :]
        return df

    def __pv_properties(self, pv: str) -> pd.DataFrame:
        """Retrieve properties of a specific PV from the archiver.

        Args:
            pv (str): Name of the Process Variable.

        Returns:
            pd.DataFrame: DataFrame containing the PV's properties.

        Raises:
            ValueError: If the PV is not found in the archiver.
            Warning: If multiple PVs match the search criteria.

        Note:
            Only the first matching PV's properties are returned if multiple matches exist.
        """
        url_components: list = [
            self.__ARCHIVER_URL,
            self.__CHANNEL_FINDER,
            f'~name={pv}'
        ]
        url = "".join(url_components)
        properties = self.__http_request(url)
        if len(properties) == 0: raise ValueError(f'PV {pv} not found.')
        if len(properties) == 0: warnings.warn('Multiple PVs retrieved, only the first one will be returned.')

        return pd.DataFrame(properties[0]['properties'])

    def download_data(self, pv_name: str, 
                     start: datetime, 
                     end: datetime,
                     verbose: bool = False) -> PV:
        """Download and process data for a specific PV.

        This method handles the complete data download process, including:
        1. Verifying the requested time range
        2. Downloading raw data
        3. Filtering data to the exact requested range
        4. Creating a PV object with the processed data

        Args:
            pv_name (str): Name of the Process Variable to download.
            start (datetime): Start time for data retrieval in EPICS timezone.
            end (datetime): End time for data retrieval in EPICS timezone.
            verbose (bool, optional): If True, prints progress information.
                Defaults to False.

        Returns:
            PV: A PV object containing the downloaded and processed data.

        Raises:
            AssertionError: If the start time is not before the end time.

        Note:
            The method automatically handles timezone conversions and ensures
            the returned data exactly matches the requested time range.
        """
        start_ts: int = int(start.timestamp())
        end_ts: int = int(end.timestamp())
        assert start_ts < end_ts, 'Invalid: start date must be before end date'
        df: pd.DataFrame
        
        if verbose: 
            sep = '=' * os.get_terminal_size().columns
            print(sep)
            print(f"Downloading data for pv {pv_name}")
        pv_properties = self.__pv_properties(pv_name)

        df = self.__download_data(pv_name, start, end, verbose=verbose)
        df = self.__filter_data(df, start_ts, end_ts)

        # Convert timestamps to EPICS timezone
        datetime_series = pd.to_datetime(df['secs'] + df['nanos']*1e-9, unit='s', utc=True)
        datetime_series = datetime_series.dt.tz_convert(start.tzinfo)
        df = df.set_index(pd.DatetimeIndex(datetime_series, name='datetime'))
        df = df.drop(columns=['secs', 'nanos'])

        if verbose:
            print(f'First timestamp: {df.index[0]}')
            print(f'Last timestamp: {df.index[-1]}')
            print(sep)

        pv: PV = PV(name=pv_name, raw_data=df, properties=pv_properties)
            
        return pv
