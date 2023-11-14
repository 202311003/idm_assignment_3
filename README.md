# idm_assignment_3
# Cricket Data Scraping

This repository contains Python scripts for scraping cricket player attributes and match schedules from multiple sources using Python. The data is collected and processed into CSV files for further analysis.

## Player Attributes

### Description
The script extracts cricket player attributes such as name, team, role, etc., from JSON files containing match details. It then compiles this information into a CSV file for analysis.

### Usage in Google Colab

1. **Install Dependencies:**
   Run the following cell in your Colab notebook:
    ```python
    !pip install pandas
    ```

2. **Run the Player Attributes Script:**
   Open the `player_attributes_scraper.ipynb` notebook in Colab and execute the cells.

### Output
The script generates a CSV file (`player_attributes.csv`) with player attributes.

## Match Schedules

### Description
The script extracts cricket match schedules, including teams, dates, venues, and other details, from multiple JSON files. It compiles this information into a CSV file for easy analysis.

### Usage in Google Colab

1. **Install Dependencies:**
   Run the following cell in your Colab notebook:
    ```python
    !pip install pandas
    ```

2. **Run the Match Schedules Script:**
   Open the `match_schedules_scraper.ipynb` notebook in Colab and execute the cells.

### Output
The script generates a CSV file (`match_schedules.csv`) with match schedules.

