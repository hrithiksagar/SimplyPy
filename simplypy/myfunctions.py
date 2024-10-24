from math import radians, cos, sin, asin, sqrt
import json
import yaml
import csv
# JSON

def open_json(file_path: str):
    """
    Open a JSON file and return its content
    :param file_path: path to the JSON file
    :return: contents of te JSON file
    """
    with open(file_path, "r") as f:
        return json.load(f)
    
def write_json(file_path: str, data: str):
    """
    Write data to a JSON file
    :param file_path: Path to the file
    :param data: Data to write to the JSON file as a dictionary 
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


# YAML 

def open_yaml(file_path: str):
    """
    Open a YAML file and return its contents.
    :param file_path: Path to the YAML file.
    :return: Contents of the YAML file as a Python object.
    """
    with open(file_path, 'r')as f:
        return yaml.safe_load(f)
    
def write_yaml(file_path, data):
    """
    Write data to a YAML file.
    :param file_path: Path to the YAML file.
    :param data: Data to write to the file as a dictionary.
    """
    with open(file_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)
                
# CSV


def read_csv(file_path: str):
    with open(file_path, mode = 'r', newline='') as file:
        reader = csv.reader(file)
        return [row for row in reader]
    
 
def write_csv(file_path: str, data: list):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
           
import pandas as pd

def read_csv_pandas(file_path: str):
    return pd.read_csv(file_path)

def write_csv_pandas(dataframe: pd.DataFrame, file_path: str):
    dataframe.to_csv(file_path, index=False)