"""
get_data.py

This script serves as the main entry point for fetching football team results from the Understat API 
for a specified season. It utilizes asynchronous programming to efficiently retrieve data and 
relies on helper functions and constants defined in separate modules.

Imports:
--------
- constants: This module is expected to contain constant values such as `name_of_team` and `season` 
  that are used throughout the script.
- helper_functions: This module is expected to include various helper functions, particularly 
  `get_team_results_from_understat`, which is used to fetch team results.

Execution Flow:
---------------
1. An asyncio event loop is created to handle asynchronous operations.
2. The script calls the `get_team_results_from_understat` function, passing in the `name_of_team` 
   and the appropriate season from the `season` list (specifically, the sixth element of the list).
3. The event loop runs until the asynchronous operation is completed, ensuring that the data 
   retrieval process is handled properly.

Usage:
------
To run this script, ensure that the necessary constants and helper functions are defined in their 
respective modules. The script can be executed in an environment that supports Python asyncio 
and has access to the Understat API.
"""

from constants import *
from helper_functions import *


loop = asyncio.get_event_loop()
loop.run_until_complete(
    get_team_results_from_understat(name_of_team, season[3]))
