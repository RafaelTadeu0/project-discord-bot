import yaml
from yaml.loader import SafeLoader

def read_yaml(file_name):
    with open(file_name, 'r') as f:
        data = yaml.load(f, Loader=SafeLoader)
    return data