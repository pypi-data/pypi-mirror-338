# EPICS Archiver Tools

[![PyPI version](https://badge.fury.io/py/epics-archiver-tools.svg)](https://badge.fury.io/py/epics-archiver-tools)
[![Python versions](https://img.shields.io/pypi/pyversions/epics-archiver-tools.svg)](https://pypi.org/project/epics-archiver-tools/)
[![License](https://img.shields.io/pypi/l/epics-archiver-tools.svg)](https://pypi.org/project/epics-archiver-tools/)

A Python library for interacting with EPICS archiver data. This tool allows you to easily download and process data from EPICS archiver servers.

## 📑 Table of Contents

- [✨ Features](#-features)
- [⚙️ Installation](#️-installation)
- [📦 Dependencies](#-dependencies)
- [🚀 Getting Started](#-getting-started)
- [🔧 Configuration](#-configuration)
- [🤝 Contributing](#-contributing)
- [📝 Citing](#-citing)
- [📄 License](#-license)
- [💬 Support](#-support)

## ✨ Features

- 📥 Download raw data from Process Variables (PVs)
- 🧩 Impute missing values
- 🧮 Match data from multiple PVs for defined timespans
- 🌐 Configurable archiver server URL
- 📊 Pandas DataFrame integration

## ⚙️ Installation

### Using pip
You can install this package through `pip`:
```bash
pip install epics-archiver-tools
```

### From source
If you want to install from source:
```bash
git clone https://github.com/andrea-pollastro/epics-archiver-tools.git
cd archivertools
pip install -e .
```

## 📦 Dependencies

This package requires:
- Python >= 3.10
- numpy >= 1.26.3
- pandas >= 2.1.4
- python-dateutil >= 2.8.2
- pytz >= 2023.3
- urllib3 >= 2.0.0
- tqdm >= 4.65.0

## 🚀 Getting Started

Interactions with the archiver are managed by the `ArchiverClient` class. Let's see some examples.

### 📥 Single PV data downloading
To download the data of a given PV, refer to the `.download_data()` function:

```python
from datetime import datetime
from archivertools import ArchiverClient

# Initialize the client with your archiver server URL
archiver_client = ArchiverClient(archiver_url="http://your-archiver-server")

pv = archiver_client.download_data(
    pv_name='YOUR_PV_NAME',
    precision=100,  # this defines the precision of your signal in ms
    start=datetime(year=2023, month=4, day=25, hour=22),
    end=datetime(year=2023, month=4, day=25, hour=23),
    verbose=False,
)
```

The returned `PV` object contains:
```python
pv.name  # PV name (string)
pv.raw_data  # Raw data as pandas.DataFrame
pv.clean_data  # Cleaned data as pandas.DataFrame
pv.properties  # PV properties as pandas.DataFrame
pv.first_timestamp  # First timestamp as datetime
pv.last_timestamp  # Last timestamp as datetime
```

### 🧮 Data matching
For a given `list` of PVs, data can be matched according to their timestamps. The list must be a sequence of `str`.
PVs could have different archiving policies. In order to have a matching on the timestamps, they must follow the same 
archiving policy (this means that all the archiving policies of the listed PVs must be reduced to a common archiving 
policy). The parameter `precision` allows to select the precision of the individual PVs to allow the data matching.

Example:
```python
pv_list = ['PV_NAME_1', 'PV_NAME_2']
matched_data = archiver_client.match_data(
    pv_list=pv_list,
    precision=100,
    start=datetime(year=2023, month=4, day=25, hour=22),
    end=datetime(year=2023, month=4, day=25, hour=23),
)
```

## 🔧 Configuration

The `ArchiverClient` can be configured with:
- `archiver_url`: The URL of your EPICS archiver server (default: "http://localhost:17665")
- `check_connection`: Whether to verify the connection on initialization (default: True)

Example:
```python
# Initialize without connection check
client = ArchiverClient(archiver_url="http://your-server:17665", check_connection=False)

# Or initialize with connection check
client = ArchiverClient(archiver_url="http://your-server:17665", check_connection=True)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📝 Citing

This package was developed in 2023 during my stay at Berkeley, hosted by the Accelerator Physics Group (ALS, LBNL). It was used throughout the experimental phase that led to the publication [Application of deep learning methods for beam size control during user operation at the Advanced Light Source](https://journals.aps.org/prab/abstract/10.1103/PhysRevAccelBeams.27.074602).

If you use this package in your work, please cite:
```bibtex
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

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💬 Support

For support, please open an issue in the [GitHub repository](https://github.com/andrea-pollastro/epics-archiver-tools).
