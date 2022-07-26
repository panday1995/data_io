# data_io

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg) <!--(https://opensource.org/licenses/MIT)-->
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)

`data_io` facilitates your data storage and retrieval in the KR project.

## Installation

```shell
python -m pip install "git+https://{your_user_name}:{your_password}@source.coderefinery.org/krproject/architecture/utils/data_io.git#egg=data_io"
```

## Usage

To use the package, a `schema.yaml` file to specify. Currently, the template `schema.yaml` looks like:

```yaml
FILE_NAME: test_out.csv
PATH: //plan-fs2.srv.aau.dk/Fileshares/KRproject/data
pkg_name: test_pkg 
```

Any suggestions on modifying the file is super welcomed. </br>

With the `schema.file` as a configuration file, one can use the `data_io` package as:

```python
from data_io import DataStore, DataRetri

config = "schema.yaml"

# to retrieve data from a path and read in as a DataFrame
df = DataRetri(config)

# to store data into a path as a .csv file
DataStore(df, config)

```
