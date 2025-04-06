from .services.data_downloader import DataDownloader
from .services.data_preprocesser import DataPreprocesser
from .pv import PV
from datetime import datetime
from typing import List, Union
from tqdm import tqdm
import pandas as pd
import warnings


class ArchiverClient:
    """Main client class for interacting with EPICS archiver data.

    This class provides a high-level interface for downloading and processing data from EPICS archiver servers.
    It handles data retrieval, preprocessing, and matching of multiple Process Variables (PVs).

    Attributes:
        __data_downloader (DataDownloader): Handles data retrieval from the archiver server.
        __data_preprocesser (DataPreprocesser): Handles data cleaning and preprocessing.

    Example:
        >>> from archivertools import ArchiverClient
        >>> client = ArchiverClient()
        >>> pv = client.download_data(
        ...     pv_name="YOUR_PV",
        ...     precision=100,
        ...     start=datetime(2023, 4, 25, 22),
        ...     end=datetime(2023, 4, 25, 23)
        ... )
    """

    def __init__(self):
        """Initialize the ArchiverClient with data downloader and preprocessor."""
        self.__data_downloader = DataDownloader()
        self.__data_preprocesser = DataPreprocesser()

    def download_data(self, pv_name: str,
                     precision: int,
                     start: datetime,
                     end: datetime,
                     verbose: bool = False) -> PV:
        """Download and preprocess data for a single Process Variable (PV).

        Args:
            pv_name (str): Name of the Process Variable to download.
            precision (int): Data sampling rate in milliseconds. This defines the precision
                of the signal and must be compatible with the PV's archiving policy.
            start (datetime): Start time for data retrieval in local timezone.
            end (datetime): End time for data retrieval in local timezone.
            verbose (bool, optional): If True, prints progress information. Defaults to False.

        Returns:
            PV: A PV object containing the downloaded and preprocessed data.

        Example:
            >>> from datetime import datetime
            >>> pv = client.download_data(
            ...     pv_name="SR04C___QFA____AM00",
            ...     precision=100,
            ...     start=datetime(2023, 4, 25, 22),
            ...     end=datetime(2023, 4, 25, 23)
            ... )
        """
        pv: PV = self.__data_downloader.download_data(
            pv_name, start, end, verbose
        )
        pv = self.__data_preprocesser.clean_data(pv, precision)
        return pv

    def __match_data(self, pv_list: List[PV],
                    precision: int,
                    verbose: bool = True) -> pd.DataFrame:
        """Match data from multiple PVs based on their timestamps.

        This is an internal method that handles the actual data matching process.

        Args:
            pv_list (List[PV]): List of PV objects to match.
            precision (int): Common precision to use for all PVs in milliseconds.
            verbose (bool, optional): If True, prints progress information. Defaults to True.

        Returns:
            pd.DataFrame: A DataFrame containing the matched data from all PVs.

        Note:
            All PVs must have compatible archiving policies for successful matching.
        """
        return self.__data_preprocesser.match_data(pv_list, precision, verbose)

    def match_data(self, pv_list: List[str],
                  precision: int,
                  start: datetime,
                  end: datetime,
                  verbose: int = 0) -> pd.DataFrame:
        """Match data from multiple PVs over a specified time range.

        This method downloads and matches data from multiple PVs, ensuring they are aligned
        by their timestamps. All PVs must have compatible archiving policies.

        Args:
            pv_list (List[str]): List of PV names to download and match.
            precision (int): Common precision to use for all PVs in milliseconds.
            start (datetime): Start time for data retrieval in local timezone.
            end (datetime): End time for data retrieval in local timezone.
            verbose (int, optional): Verbosity level (0: silent, 1: progress, 2: detailed).
                Defaults to 0.

        Returns:
            pd.DataFrame: A DataFrame containing the matched data from all PVs.

        Example:
            >>> pv_list = ["PV1", "PV2", "PV3"]
            >>> matched_data = client.match_data(
            ...     pv_list=pv_list,
            ...     precision=100,
            ...     start=datetime(2023, 4, 25, 22),
            ...     end=datetime(2023, 4, 25, 23)
            ... )

        Note:
            All PVs must have compatible archiving policies for successful matching.
            The precision parameter must be compatible with all PVs' archiving policies.
            The input must be a sequence of strings. Each string represents a Process Variable (PV) name.
            The archiving policy of each PV must be compatible with the specified precision.
            For example, if a PV is archived every 100ms, using a precision of 50ms will result in missing data.
            It's recommended to check the archiving policy of each PV before matching to ensure data consistency.
        """
        assert all(filter(lambda x: isinstance(x, str), pv_list)), 'please use only lists of strings.'
        verbose_download = verbose == 2
        verbose_match = verbose > 0
        pv_list_obj: List[PV] = []
        pbar = tqdm(pv_list)
        for pv in pbar:
            pbar.set_description(f"Downloading PV {pv}")
            try:
                pv = self.download_data(pv, precision, start, end, verbose_download)
                pv_list_obj.append(pv) # type: ignore
            except:
                warnings.warn(f'An error occurred while fetching {pv} data. PV skipped.')
        return self.__match_data(pv_list_obj, precision, verbose_match) # type: ignore