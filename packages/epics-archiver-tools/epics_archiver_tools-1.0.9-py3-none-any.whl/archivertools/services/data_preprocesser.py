from typing import List
from ..pv import PV
from tqdm import tqdm
import pandas as pd
import os

class DataPreprocesser:
    """Handles data preprocessing and matching for EPICS archiver data.

    This class provides methods for cleaning and matching data from multiple PVs,
    including missing value imputation and timestamp alignment.

    Note:
        The preprocessing steps ensure data consistency and proper alignment
        across multiple PVs with potentially different archiving policies.
    """
    
    def clean_data(self, pv: PV, precision: int) -> PV:
        """Clean and impute missing values in PV data.

        This method processes raw PV data by:
        1. Removing severity and status columns
        2. Resampling data to the specified precision
        3. Forward-filling missing values
        4. Formatting timestamps
        5. Handling the initial NaN value

        Args:
            pv (PV): The PV object containing raw data to clean.
            precision (int): Data sampling rate in milliseconds.

        Returns:
            PV: The input PV object with cleaned data stored in its clean_data attribute.

        Note:
            The precision parameter should be compatible with the PV's archiving policy
            to ensure proper data imputation.
        """
        pv.clean_data = pv.raw_data.drop(columns=['severity', 'status'])
        pv.clean_data = pv.clean_data.resample(f'{precision}ms').ffill()
        pv.clean_data.index = pv.clean_data.index.strftime('%Y-%m-%d %H:%M:%S.%f') # type: ignore
        pv.clean_data['val'][0] = pv.clean_data['val'][1] # first value is always NaN

        return pv
    
    def match_data(self, pv_list: List[PV], precision: int, verbose: bool = False) -> pd.DataFrame:
        """Match and align data from multiple PVs.

        This method processes and matches data from multiple PVs by:
        1. Cleaning each PV's data
        2. Aligning timestamps to the specified precision
        3. Merging data from all PVs into a single DataFrame

        Args:
            pv_list (List[PV]): List of PV objects to match.
            precision (int): Common precision to use for all PVs in milliseconds.
            verbose (bool, optional): If True, prints progress information.
                Defaults to False.

        Returns:
            pd.DataFrame: A DataFrame containing matched data from all PVs.
                The index contains timestamps, and columns contain values from each PV.

        Note:
            All PVs must have compatible archiving policies for successful matching.
            The precision parameter must be compatible with all PVs' archiving policies.
        """
        pbar = tqdm(pv_list)
        for pv in pbar:
            pbar.set_description(f"Cleaning data PV {pv.name}")
            pv = self.clean_data(pv, precision)
        
        def extract_data(pv: PV) -> pd.DataFrame:
            """Extract and rename data from a PV object.

            Args:
                pv (PV): The PV object to extract data from.

            Returns:
                pd.DataFrame: DataFrame containing the PV's data with renamed columns.
            """
            data: pd.DataFrame = pv.clean_data
            data = data.rename(columns={'val': pv.name})
            return data
        
        matched_data: pd.DataFrame = extract_data(pv_list[0])
        for pv in pv_list[1:]:
            matched_data = matched_data.merge(extract_data(pv), on=['datetime'])
        
        if verbose:
            sep = '=' * os.get_terminal_size().columns
            print(sep)
            print(f'PV matched: {[pv_name for pv_name in matched_data.columns]}')
            print(f'First timestamp: {matched_data.index[0]}')
            print(f'Last timestamp: {matched_data.index[-1]}')
            print(sep)

        return matched_data