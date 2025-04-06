# ArchiverTools

A Python library for interacting with EPICS archiver data. This tool allows you to easily download, process, and analyze data from EPICS archiver servers.

## ✨ Features

- 📥 Download raw data from Process Variables (PVs)
- 🧩 Impute missing values
- 🧮 Match data from multiple PVs for defined timespans
- 🌐 Configurable archiver server URL

## ⚙️ Installation

You can install this package through `pip`:
```
pip install epics-archiver-tools
```

## 🚀 Getting started
Interactions with the archiver are managed by the `ArchiverClient` class. Let's see some examples.

### 📥 Single PV data downloading
To download the data of a given PV, refer to the `.download_data()` function:

``` python
from datetime import datetime
from archivertools import ArchiverClient

# Initialize the client with your archiver server URL
archiver_client = ArchiverClient(archiver_url="http://your-archiver-server")

pv = archiver_client.download_data(
    pv_name='YOUR_PV_NAME',
    precision=100, # this defines the precision of your signal in ms (bounded by the archiving policy)
    start=datetime(year=2023, month=4, day=25, hour=22),
    end=datetime(year=2023, month=4, day=25, hour=23),
    verbose=False,
)
```
it returns a `PV` object which contains the following information:
``` python
pv.name # pv name, string
pv.raw_data # pv raw data as a pandas.DataFrame object
pv.clean_data # pv clean data as a pandas.DataFrame object
pv.properties # pv properties stored on the archiver as a pandas.DataFrame object
pv.first_timestamp # first timestamp of the downloaded timestamp as a datetime object
pv.last_timestamp # last timestamp of the downloaded timestamp as a datetime object
```

### 🧮 Data matching
For a given `list` of PVs, data can be matched according to their timestamps. The list must be a sequence of `str`.
PVs could have different archiving policy. In order to have a matching on the timestamps, they must follow the same archiving policy (this means that all the archiving policies of the listed PVs must be reduced to a common archiving policy).
The parameter `precision` allows to select the precision of the individual PVs to allow the data matching

Data matching can be done using the `.match_data()` function:

``` python
... # all your fancy code
pv_list = ['PV_NAME_1', 'PV_NAME_2']
matched_data = archiver_client.match_data(
    pv_list=pv_list,
    precision=100,
    start=datetime(year=2023, month=4, day=25, hour=22),
    end=datetime(year=2023, month=4, day=25, hour=23),
)
``` 

## 🔧 Configuration

The `ArchiverClient` can be configured with the following parameters:
- `archiver_url`: The URL of your EPICS archiver server (default: "http://localhost:17665")
- `check_connection`: Whether to verify the connection to the archiver server on initialization (default: True)

Example:
```python
# Initialize without connection check
client = ArchiverClient(archiver_url="http://your-server:17665", check_connection=False)

# Or initialize with connection check
client = ArchiverClient(archiver_url="http://your-server:17665", check_connection=True)
```

## 📝 Citing
This package was developed in 2023 during my stay at Berkeley, hosted by the Accelerator Physics Group (ALS, LBNL). It was used throughout the experimental phase that led to the publication <a href="https://journals.aps.org/prab/abstract/10.1103/PhysRevAccelBeams.27.074602">Application of deep learning methods for beam size control during user operation at the Advanced Light Source</a>.

If you use this package in your work, please cite the following paper:
```
@article{hellert2024application,
  title={Application of deep learning methods for beam size control during user operation at the Advanced Light Source},
  author={Hellert, Thorsten and Ford, Tynan and Leemann, Simon C and Nishimura, Hiroshi and Venturini, Marco and Pollastro, Andrea},
  journal={Physical Review Accelerators and Beams},
  volume={27},
  number={7},
  pages={074602},
  year={2024},
  publisher={APS}
}
```