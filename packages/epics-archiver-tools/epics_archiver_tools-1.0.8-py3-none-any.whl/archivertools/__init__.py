"""
ArchiverTools - A Python library for interacting with EPICS archiver data.

This package provides tools for downloading, processing, and analyzing data from EPICS archiver servers.
It supports data retrieval, missing value imputation, and data matching across multiple Process Variables (PVs).

Example:
    >>> from archivertools import ArchiverClient
    >>> client = ArchiverClient(archiver_url="http://your-server:17665")
    >>> data = client.download_data(pv_name="YOUR_PV", start=start_time, end=end_time)
"""

from .archiver_client import ArchiverClient
from .archiving_policy import ArchivingPolicy
from .pv import PV

__all__ = [
    'archiver_client',
    'archiving_policy',
    'pv',
]

__author__ = 'Andrea Pollastro'
__author_email__ = 'apollastro@lbl.gov'