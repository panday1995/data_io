"""This is an utility module to store data into the group folder of KR project
Created on Jul 15, 2022

@author: Fan Yang

Todo:


"""
import os
import pandas as pd
import pickle

from data_io.yml_config import cfg


class DataStore:
    """This class creates an object for data storage
    """

    def __init__(
        self,
        data,
        yml_file="schema.yaml"
    ) -> None:
        self.data_to_store = data
        self.cfg_dict = cfg(yml_file)

    def store_to(self):
        dir_path = self.cfg_dict["OUTPUT_PATH"]
        file_name = self.cfg_dict["OUTPUT_FILE"]
        file_path = os.path.join(dir_path, file_name)
        try:
            self.data_to_store.to_csv(file_path)
        except AttributeError as error:
            print("export as .csv file is not support, the data is stored as .pickle file")
            with open(file_path.split()[0]+".pickle", 'wb') as data_file:
                pickle.dump(self.data_to_store, data_file)
        print(f"The file is stored at {file_path}")
        return file_path


class DataRetri:
    """This class creates an object for data retrieval
    """

    def __init__(
        self,
        yml_file="schema.yaml"
    ) -> None:
        self.cfg_dict = cfg(yml_file)

    def _read_input(self, file_name):
        input_ls = self.cfg_dict["INPUT"]
        for input_file in input_ls:
            if file_name in input_file["INPUT_FILE"]:
                return input_file["INPUT_PATH"], input_file["INPUT_FILE"]
            else:
                print("file not registered in the config file")

    def _retrieve_data(self, file_path):
        try:
            data = pd.read_csv(file_path)
        except:
            print(
                "ParserError: import as pd.DataFrame is not support, the data is retrieved through pickle.load")
            with open(file_path.split()[0]+".pickle", 'rb') as data_file:
                data = pickle.load(data_file)
        print(f"The file is retrived at {file_path}")
        return data

    def retrieve_one(self, file_name):
        dir_path, file_name = self._read_input(file_name)
        file_name = self.cfg_dict
        file_path = os.path.join(dir_path, file_name)

        return self._retrieve_data(file_path)

    def retrieve_all(self):
        data_dict = {}
        for input_file in self.cfg_dict["INPUT"]:
            dir_path, file_name = input_file["INPUT_PATH"], input_file["INPUT_FILE"]
            file_path = os.path.join(dir_path, file_name)
            data = self._retrieve_data(file_path)
            data_dict[file_name] = data

        return data_dict
