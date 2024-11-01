"""
extract_load_data.py

This script is designed to extract data from JSON files and convert them into CSV format. 
It serves as a utility for loading and processing data in a structured manner.

Imports:
--------
- constants: This module is expected to contain constant values and configuration settings 
  that are utilized throughout the script.
- helper_functions: This module is expected to include various helper functions, particularly 
  `list_json_files` and `convert_all_json`, which are used to list JSON files and convert 
  them to CSV format, respectively.

Execution Flow:
---------------
1. The script defines the `json_directory`, which specifies the directory path containing the 
   JSON files to be processed. By default, it is set to the current directory ("."), but 
   this can be modified to point to any specific directory.
2. The `list_json_files` function is called to retrieve a list of JSON files located in the 
   specified directory.
3. The `convert_all_json` function is called with the list of JSON files to convert each 
   file to CSV format.

Usage:
------
To run this script, ensure that the necessary constants and helper functions are defined in 
their respective modules. The script can be executed in an environment that has access to the 
Pandas library for data manipulation.
"""
from constants import *
from helper_functions import *

json_directory = "."  # Or your directory path
json_file_list = list_json_files(json_directory)
convert_all_json(json_file_list)
