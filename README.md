# Bayern Munich Performance Analytics

Welcome to the **Bayern Munich Performance Analytics** repository! This project focuses on analyzing the performance of Bayern Munich in the Bundesliga using advanced metrics like expected goals (xG) and expected goals against (xGA). The analysis leverages data collected from Understat and Transfermarkt to provide insights into team performance over various seasons.

## Table of Contents
- [Project Overview](#project-overview)
- [Data Collection](#data-collection)
- [Project Structure](#project-structure)
- [Analysis and Visualizations](#analysis-and-visualizations)
- [Usage](#usage)
- [Requirements](#requirements)

## Project Overview
This project aims to assess and visualize the performance of Bayern Munich over the seasons from 2018 to 2023, focusing on key performance indicators such as xG and xGA. By analyzing these metrics, we can gain insights into the team's strengths and weaknesses, as well as track performance trends over time.

## Data Collection
Data for this project was gathered using the following scripts:
- **`get_data.py`**: Fetches match results from the Understat API for the specified season.
- **`extract_load_data.py`**: Extracts data from JSON files and converts it into CSV format for easy analysis.

Data sources include:
- [Understat](https://understat.com/)
- [Transfermarkt](https://www.transfermarkt.com/)

## Project Structure
```
bayern-munich-performance-analytics/
│
├── Data for Bayern Munich/
│   ├── 2018-2019.csv
│   ├── 2019-2020.csv
│   └── ... (CSV files for each season)
│
├── Power BI/
│   ├── Bayern_Munich_Analytics.pbix
│   ├── Bayern_Munich_Analytics.pdf
│   └── Bayern_Munich_Analytics.png
│
├── Data for Managers/
│   └── managers_data.csv
│
├── JSON Files/
│   ├── 2018-2019.json
│   ├── 2019-2020.json
│   └── ... (JSON files for each season)
│
├── scripts/
│   ├── constants.py
│   ├── helper_functions.py
│   ├── get_data.py
│   └── extract_load_data.py
│
└── README.md
```

## Analysis and Visualizations
The analysis includes detailed visualizations created using Power BI, showcasing the performance metrics of Bayern Munich across different seasons. The Power BI files can be found in the `Power BI` directory.
Here is a sample visualization of Bayern Munich's performance:
![Bayern Munich Performance Visualization](image/Bayern_Munich_Analytics.JPG)

## Usage
To use the scripts for data collection and processing:
1. Clone the repository to your local machine.
2. Ensure you have the necessary libraries installed.
3. Run the `get_data.py` script to collect match results and save them in JSON format.
4. Execute the `extract_load_data.py` script to convert JSON files into CSV format.

## Requirements
- Python 3.x
- Pandas
- Aiohttp
- Understat
- power BI Desktop 


