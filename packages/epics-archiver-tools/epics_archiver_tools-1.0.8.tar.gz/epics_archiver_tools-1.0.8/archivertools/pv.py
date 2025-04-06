from .archiving_policy import ArchivingPolicy
import pandas as pd

class PV:
    """Represents a Process Variable (PV) entity from the EPICS archiver.

    This class encapsulates all data and metadata associated with a single PV,
    including its raw data, properties, cleaned data, and archiving policy.

    Attributes:
        name (str): Name of the Process Variable.
        raw_data (pd.DataFrame): Raw data downloaded from the archiver.
        properties (pd.DataFrame): PV properties as reported in the archiver.
        clean_data (pd.DataFrame): Cleaned data with missing values imputed.
        first_timestamp (pd.Timestamp): First timestamp in the data timespan.
        last_timestamp (pd.Timestamp): Last timestamp in the data timespan.
        archiving_policy (ArchivingPolicy): Archiving policy from the archiver.

    Note:
        The clean_data and archiving_policy attributes have setters, but it's
        recommended to only modify these through the appropriate service classes
        to maintain data consistency.
    """

    def __init__(self, name: str, raw_data: pd.DataFrame, properties: pd.DataFrame):
        """Initialize a PV object with its basic data and properties.

        Args:
            name (str): Name of the Process Variable.
            raw_data (pd.DataFrame): Raw data downloaded from the archiver.
            properties (pd.DataFrame): PV properties from the archiver.

        Note:
            The archiving policy is automatically extracted from the properties
            during initialization.
        """
        self.__name: str = name
        self.__raw_data: pd.DataFrame = raw_data
        self.__properties: pd.DataFrame = properties
        self.__clean_data: pd.DataFrame = None  # type: ignore
        self.__first_timestamp: pd.Timestamp = raw_data.index[0] # type: ignore
        self.__last_timestamp: pd.Timestamp = raw_data.index[-1] # type: ignore

        def __extract_archiving_policy(pv_properties: pd.DataFrame) -> ArchivingPolicy:
            """Extract the archiving policy from PV properties.

            This private method converts the archiving policy string from the archiver
            into an ArchivingPolicy enum value.

            Args:
                pv_properties (pd.DataFrame): DataFrame containing PV properties.

            Returns:
                ArchivingPolicy: The corresponding archiving policy enum value.

            Note:
                The method handles various policy strings including 'veryfast', 'fast',
                'medium', 'slow', and 'veryslow'.
            """
            ap_str = pv_properties[pv_properties['name'] == 'archive']['value'].values[0]
            ap_str = ap_str.lower().strip().replace('controlled', '')
            ap: ArchivingPolicy = ArchivingPolicy.FAST
            match ap_str:
                case 'veryfast':
                    ap = ArchivingPolicy.VERYFAST
                case 'fast':
                    ap = ArchivingPolicy.FAST
                case 'medium':
                    ap = ArchivingPolicy.MEDIUM
                case 'slow':
                    ap = ArchivingPolicy.SLOW
                case 'veryslow':
                    ap = ArchivingPolicy.VERYSLOW
            return ap
        self.__archiving_policy: ArchivingPolicy = __extract_archiving_policy(properties)

    @property
    def archiving_policy(self) -> ArchivingPolicy:
        """Get the PV's archiving policy.

        Returns:
            ArchivingPolicy: The current archiving policy of the PV.
        """
        return self.__archiving_policy
    
    @archiving_policy.setter
    def archiving_policy(self, archiving_policy) -> None:
        """Set the PV's archiving policy.

        Args:
            archiving_policy (ArchivingPolicy): The new archiving policy to set.

        Note:
            Changing the archiving policy should be done with caution as it affects
            data processing and matching operations.
        """
        self.__archiving_policy = archiving_policy

    @property
    def first_timestamp(self) -> pd.Timestamp:
        """Get the first timestamp in the PV's data.

        Returns:
            pd.Timestamp: The earliest timestamp in the data.
        """
        return self.__first_timestamp
    
    @property
    def last_timestamp(self) -> pd.Timestamp:
        """Get the last timestamp in the PV's data.

        Returns:
            pd.Timestamp: The latest timestamp in the data.
        """
        return self.__last_timestamp
    
    @property
    def name(self) -> str:
        """Get the PV's name.

        Returns:
            str: The name of the PV.
        """
        return self.__name

    @property
    def raw_data(self) -> pd.DataFrame:
        """Get the raw data downloaded from the archiver.

        Returns:
            pd.DataFrame: The raw data as downloaded from the archiver.
        """
        return self.__raw_data
    
    @property
    def properties(self) -> pd.DataFrame:
        """Get the PV's properties from the archiver.

        Returns:
            pd.DataFrame: The properties as reported by the archiver.
        """
        return self.__properties
    
    @property
    def clean_data(self) -> pd.DataFrame:
        """Get the cleaned data with missing values imputed.

        Returns:
            pd.DataFrame: The cleaned and processed data.
        """
        return self.__clean_data
    
    @clean_data.setter
    def clean_data(self, clean_data: pd.DataFrame) -> None:
        """Set the cleaned data.

        Args:
            clean_data (pd.DataFrame): The cleaned data to set.

        Note:
            This should typically be set by the data preprocessing service
            to ensure proper data cleaning and consistency.
        """
        self.__clean_data = clean_data

    def __repr__(self):
        """Return a string representation of the PV.

        Returns:
            str: A string containing the PV's name, timestamp range, and archiving policy.
        """
        return f'name:{self.name}, first timestamp:{self.first_timestamp}, last timestamp:{self.last_timestamp}, archiving policy:{self.archiving_policy}'