# A small test for the haversine function: 
import simplypy
from simplypy import myfunctions
import json
from simplypy.myfunctions import * 
# haversine, open_json, read_json, write_json

def test_haversine():
    # Amsterdam to Berlin
    assert myfunctions.haversine(
        4.895168, 52.370216, 13.404954, 52.520008
    ) == print(576.6625818456291)
    
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