import pytest
import yaml
import os
import pandas as pd

from data_io.data_io import DataStore, DataRetri
from data_io.yml_config import cfg

data_to_store = pd.DataFrame({"a": [1, 2, 3, 4], "b": [2, 3, 4, 6]})

# yml_dict = dict(pkg_name="test_pkg",
#                 PATH=r"//plan-fs2.srv.aau.dk/Fileshares/KRproject/data",
#                 FILE_NAME="test.csv")
# with open("test.yaml", "w") as yml:
#     yaml.dump(yml_dict, yml)


class TestYmlConfig:
    def test_cfg(self):
        cfg_dict = cfg("test.yaml")
        assert isinstance(cfg_dict, dict)
        assert cfg_dict["pkg_name"] == "test_pkg"
        assert cfg_dict["OUTPUT_PATH"] == r"//plan-fs2.srv.aau.dk/Fileshares/KRproject/data"
        assert cfg_dict["OUTPUT_FILE"] == "test.csv"


class TestDataStore:

    def test_init(self):
        assert DataStore(data_to_store, "test.yaml")

    def test_store_to(self):
        file_path = DataStore(data_to_store, "test.yaml").store_to()
        assert os.path.exists(file_path)


class TestDataRetri:

    def test_init(self):
        assert DataRetri("test.yaml")

    def test_retrieve_from(self):
        data = DataRetri("test.yaml").retrieve_from()
        assert isinstance(data, pd.DataFrame or pd.Series)
