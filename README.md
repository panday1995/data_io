# data_io

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![version](https://img.shields.io/github/v/tag/panday1995/data_io?label=version)
![License](https://img.shields.io/badge/license-MIT-green.svg) <!--(https://opensource.org/licenses/MIT)-->
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)

`data_io` facilitates your data storage and retrieval in the KR project.

## Installation

`data_io` relied on a Python package manager for its installation. Make sure `pip` is installed and added into your system environmental variables, then copy & paste the following command in your terminal.

```shell
python -m pip install "git+https://{your_user_name}:{your_password}@source.coderefinery.org/krproject/architecture/utils/data_io.git#egg=data_io"
```

## Usage

To use the package, a `schema.yaml` file must be established first. `INPUT` and `OUTPUT` must be specified. Currently, the template `schema.yaml` looks like:

```yaml
pkg_name: test

INPUT:
  - INPUT_FILE: test1.csv
    INPUT_PATH: //plan-fs2.srv.aau.dk/Fileshares/KRproject/data
  - INPUT_FILE: test2.csv
    INPUT_PATH: //plan-fs2.srv.aau.dk/Fileshares/KRproject/data

OUTPUT:
  - OUTPUT_FILE: test_out1.csv
    OUTPUT_PATH: //plan-fs2.srv.aau.dk/Fileshares/KRproject/data
  - OUTPUT_FILE: test_out2.csv
    OUTPUT_PATH: //plan-fs2.srv.aau.dk/Fileshares/KRproject/data
```

Any suggestions on modifying the file is super welcomed. </br>

With the `schema.file` as a configuration file, one can use the `data_io` package as:

```python
from data_io import DataStore, DataRetri

config = "schema.yaml"

# to retrieve all .csv files and read in as a dictionary with file_name as key and DataFrame as value
data_dict = DataRetri().retrieve_all() # equivalent to DataRetri(config=config).retrieve_all()

# to retrieve only one .csv file and read in as a DataFrame
file_name = "test.csv"
df = DataRetri().retrieve_one(file_name)

# to store a DataFrame into a path as a .csv file
data_to_store = pd.DataFrame({"a": [1, 2, 3, 4], "b": [2, 3, 4, 6]})
# if you have only one file to store/output in your package
DataStore(df).store_to()
# if you have one of the multiple files for storage/output, you need specify the file name
DataStaore(df).store_to("test2.csv")

```

## Features

- An standardized IO process for tublar data in the KR project.
- Support specifying multiple input and output files in the configuration file.
- Support retrieval from multiple `.csv` files as multiple `DataFrame`.

### Upcoming features

- coming soon.
