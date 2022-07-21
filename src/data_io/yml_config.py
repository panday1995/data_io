import yaml
from yaml.loader import FullLoader


def cfg(yml_file):

    with open(yml_file, "rb") as yml:
        cfg_dict = yaml.load(yml, Loader=FullLoader)
    return cfg_dict
