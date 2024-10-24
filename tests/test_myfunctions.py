# A small test for the haversine function: 
import simplypy
from simplypy import myfunctions
import json
from simplypy.myfunctions import * 
# haversine, open_json, read_json, write_json

# JSON

def test_open_json(tmp_path):
    # Create a sample JSON file
    data = {"name" : "John", "age": "23"}
    json_file = tmp_path/"sample_open_json.json"
    write_json(json_file, data)
    
    # Test Opening JSON
    result = open_json(json_file)
    assert result == data
    
def test_write_json(tmp_path):
    # Create a sample JSON file
    data = {"name" : "smith", "age": "95"}
    
    # Define path for new JSON
    json_file = tmp_path/"Sample_write_json.json"
    
    # Write data to new json and verify that data
    write_json(json_file, data)
    
    with open(json_file) as f:
        result = json.load(f)
        assert result == data    
        
# YAML
        
def test_open_yaml(tmp_path):
    data = {"name" : "smith", "age": "95"}
    yaml_file = tmp_path/"sample_open_yaml.yaml"
    write_yaml(yaml_file, data)
    
    result = open_yaml(yaml_file)
    assert result == data
    
    
def test_write_yaml(tmp_path):
    data = {"name" : "smith", "age": "95"}
    yaml_file = tmp_path/"sample_write_yaml.yaml"
    write_json(yaml_file, data)
    
    with open(yaml_file) as f:
        result = yaml.safe_load(f)
        assert result == data
        
        
# CVS
def test_read_csv(tmp_path):
    # Create a sample CSV file
    csv_file = tmp_path / "sample.csv"
    data = [["name", "age"], ["Alice", "30"], ["Bob", "25"]]
    write_csv(csv_file, data)

    # Test reading CSV
    result = read_csv(csv_file)
    assert result == data

def test_write_csv(tmp_path):
    # Define data to write
    data = [["city", "population"], ["New York", "8000000"], ["Los Angeles", "4000000"]]
    
    # Define path for new CSV
    csv_file = tmp_path / "new_sample.csv"
    
    # Write data and verify
    write_csv(csv_file, data)
    
    with open(csv_file, 'r') as f:
        result = [line.strip().split(',') for line in f]
        assert result == data

def test_read_csv_pandas(tmp_path):
    # Create a sample CSV file
    csv_file = tmp_path / "sample_pandas.csv"
    data = pd.DataFrame({"name": ["Alice", "Bob"], "age": [30, 25]})
    write_csv_pandas(data, csv_file)

    # Test reading CSV with Pandas
    result = read_csv_pandas(csv_file)
    pd.testing.assert_frame_equal(result, data)

def test_write_csv_pandas(tmp_path):
    # Define DataFrame to write
    data = pd.DataFrame({"city": ["New York", "Los Angeles"], "population": [8000000, 4000000]})
    
    # Define path for new CSV
    csv_file = tmp_path / "new_sample_pandas.csv"
    
    # Write DataFrame and verify
    write_csv_pandas(data, csv_file)
    
    result = pd.read_csv(csv_file)
    pd.testing.assert_frame_equal(result, data)        