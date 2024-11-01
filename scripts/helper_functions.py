import json
import asyncio
from understat import Understat
import aiohttp
import pandas as pd
import os


import os
import json
import aiohttp


async def get_team_results_from_understat(name_of_team, season):
    """
    Asynchronously retrieves team results from Understat and saves them to a JSON file.

    This function fetches match results for a specified football team during a specified season 
    using the Understat API. The results are saved in a JSON file named in the format 
    "{season}-{season+1}.json" within a directory called "JSON Files".

    Parameters:
    ----------
    name_of_team : str
        The name of the football team for which to retrieve the results.

    season : int
        The season year for which the results are to be fetched. For example, for the 2021-2022 
        season, this would be 2021.

    Returns:
    -------
    None
        This function does not return any value. It saves the results to a JSON file.

    Raises:
    ------
    aiohttp.ClientError:
        If there is an error while making the HTTP request to the Understat API.

    FileNotFoundError:
        If the JSON file cannot be created or written to the specified path.

    Notes:
    -----
    - The JSON file will contain match results, which may include information such as date, 
      opponent, score, and other relevant statistics.
    - Ensure that the Understat library is correctly installed and imported before calling this 
      function.
    """
    # Create directory if it doesn't exist
    directory = "JSON Files"
    os.makedirs(directory, exist_ok=True)

    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        results = await understat.get_team_results(
            name_of_team,
            season
        )

        # Save JSON data to a file in the "JSON Files" directory
        json_file_path = os.path.join(directory, f"{season}-{season+1}.json")
        with open(json_file_path, 'w') as f:
            json.dump(results, f, indent=4)

        print(f"JSON file downloaded successfully as {json_file_path}")


def extract_data_from_json(json_file_path):
    """
    Extracts match data and infers the season based on the match date.

    Args:
        json_file_path (str): Path to the JSON file.

    Returns:
        pandas.DataFrame: DataFrame with 'id', 'datetime', 'name_of_team', 
                          'xG', and 'season' columns.
    """

    data = []
    with open(json_file_path, 'r') as f:
        matches = json.load(f)
        for match in matches:
            if match['h']['title'] == "Bayern Munich" or match['a']['title'] == "Bayern Munich":
                match_date = pd.to_datetime(match['datetime'])
                # Determine season based on month: Aug/Sep onwards is next year
                if match_date.month >= 8:
                    season = f"{match_date.year}-{match_date.year + 1}"
                else:
                    season = f"{match_date.year - 1}-{match_date.year}"

                data.append({
                    'id': match['id'],
                    'datetime': match_date,  # Use the converted datetime
                    'name_of_team': match['h']['title'] if match['h']['title'] == "Bayern Munich" else match['a']['title'],
                    'xG': float(match['xG']['h'] if match['h']['title'] == "Bayern Munich" else match['xG']['a']),
                    'season': season  # Add the season to the data
                })

    df = pd.DataFrame(data)
    return df


def extract_data_from_json_to_df(json_file_path):
    """
    Extracts comprehensive match data from a JSON file, including 
    calculated fields like season and opponent.

    Args:
        json_file_path (str): Path to the JSON file.

    Returns:
        pandas.DataFrame: DataFrame with detailed match information.
    """

    data = []
    with open(json_file_path, 'r') as f:
        matches = json.load(f)
        for match in matches:
            if match['h']['title'] == "Bayern Munich" or match['a']['title'] == "Bayern Munich":
                match_date = pd.to_datetime(match['datetime'])
                if match_date.month >= 8:
                    season = f"{match_date.year}-{match_date.year + 1}"
                else:
                    season = f"{match_date.year - 1}-{match_date.year}"

                bayern_is_home = match['h']['title'] == "Bayern Munich"

                data.append({
                    'id': match['id'],
                    'datetime': match_date,
                    'season': season,
                    'competition': "Bundesliga",  # You might need to adjust this
                    'home_team': match['h']['title'],
                    'away_team': match['a']['title'],
                    'home_goals': int(match['goals']['h']),
                    'away_goals': int(match['goals']['a']),
                    'name_of_team': "Bayern Munich",
                    'xG': float(match['xG']['h'] if bayern_is_home else match['xG']['a']),
                    'xG_conceded': float(match['xG']['a'] if bayern_is_home else match['xG']['h']),
                    'result': match['result'].upper() if bayern_is_home else ('W' if match['result'] == 'l' else ('L' if match['result'] == 'w' else 'D')),
                    'opponent': match['a']['title'] if bayern_is_home else match['h']['title'],
                    # 'matchday': None,  # Fetch using an API or scraping if possible
                    'venue': 'Home' if bayern_is_home else 'Away'
                    # 'manager': None   # Fetch using an API or scraping if possible
                })

    df = pd.DataFrame(data)
    return df


def dataframe_to_csv(df, filename, output_dir="output"):
    """Saves a Pandas DataFrame to a CSV file.

    Args:
        df: The DataFrame to save.
        filename: The name of the CSV file (without extension).
        output_dir: The directory to save the CSV file to.  
                    Creates the directory if it doesn't exist.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create the directory

    filepath = os.path.join(output_dir, f"{filename}.csv")
    df.to_csv(filepath, index=False)  # Save to CSV, no index
    print(f"DataFrame saved to {filepath}")


def append_json_files(directory):
    """
    Appends data from all JSON files in a directory into a single Pandas DataFrame.
    Assumes each JSON file contains match data in the format expected by extract_data_from_json_.

    Args:
        directory (str): The path to the directory containing the JSON files.

    Returns:
        pandas.DataFrame: A DataFrame containing the combined data from all JSON files, or None if no JSON files are found.
    """

    all_data = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):  # Process only JSON files
            filepath = os.path.join(directory, filename)
            try:
                df = extract_data_from_json_to_df(
                    filepath)  # Use your existing function
                all_data.append(df)
            # Handle potential errors (e.g., invalid JSON)
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    if all_data:  # Check if any JSON data was successfully loaded
        combined_df = pd.concat(all_data, ignore_index=True)
        return combined_df
    else:
        print("No JSON files found or processed successfully in the directory.")
        return None


def list_json_files(directory):
    """Lists all JSON files in a directory.

    Args:
        directory (str): The path to the directory.

    Returns:
        list: A list of JSON filenames, or an empty list if no JSON files are found.
    """
    json_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            json_files.append(filename)
    return json_files


def convert_all_json(json_file_list):
    """
    Converts a list of JSON files to CSV format.

    This function iterates over a provided list of JSON file paths, extracts data from each JSON 
    file into a Pandas DataFrame, and then converts that DataFrame to a CSV file. The output 
    CSV files are saved in a specified directory, named according to the original JSON file names 
    without their extensions.

    Parameters:
    ----------
    json_file_list : list of str
        A list containing the file paths of the JSON files to be converted.

    Returns:
    -------
    None
        This function does not return any value. It saves the converted CSV files to the specified 
        output directory.

    Notes:
    -----
    - The output directory for the CSV files is hardcoded as "Data for Bayern Munich". Ensure 
      this directory exists or modify the function to create it if necessary.
    - The function assumes the existence of `extract_data_from_json_to_df` and 
      `dataframe_to_csv` functions to handle data extraction and CSV writing respectively.
    - Ensure that the necessary libraries (e.g., pandas) are imported and available in the 
      environment where this function is used.
    """
    for file in json_file_list:
        data_frame = extract_data_from_json_to_df(file)
        dataframe_to_csv(data_frame, file.split(
            ".")[0], output_dir="Data for Bayern Munich")
