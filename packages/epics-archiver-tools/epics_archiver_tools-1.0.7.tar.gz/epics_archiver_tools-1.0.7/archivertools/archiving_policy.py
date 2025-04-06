from enum import Enum

class ArchivingPolicy(Enum):
    """Represents the archiving policy levels for EPICS Process Variables.

    This enum defines the different archiving policy levels available in the EPICS archiver,
    from VERYSLOW (least frequent sampling) to VERYFAST (most frequent sampling).

    The values are ordered from 0 to 4, where higher values indicate more frequent sampling:
    - VERYSLOW (0): Least frequent sampling
    - SLOW (1): Slow sampling rate
    - MEDIUM (2): Medium sampling rate
    - FAST (3): Fast sampling rate
    - VERYFAST (4): Most frequent sampling

    Note:
        The archiving policy determines how frequently a PV's value is stored in the archiver.
        This affects the precision and storage requirements of the archived data.
    """
    VERYSLOW = 0
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    VERYFAST = 4

    def __lt__(self, other):
        """Compare two archiving policies based on their sampling frequency.

        Args:
            other (ArchivingPolicy): The other archiving policy to compare with.

        Returns:
            bool: True if this policy has a lower sampling frequency than the other,
                  False otherwise.

        Note:
            This comparison is used to determine if one policy samples less frequently
            than another. For example, VERYSLOW < FAST returns True.
        """
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented