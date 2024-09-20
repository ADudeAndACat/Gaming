import streamlit as st
import json, os
import pandas as pd  # pandas is useful for creating a DataFrame


# Load JSON data from a file
def load_json_file(filename: str) -> dict:
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        st.error(f"File {filename} does not exist.")
        return {}


# Convert JSON data to a table-friendly format
def json_to_table(data: dict) -> pd.DataFrame:
    table_data = []

    # Iterate through each date and its list of rolls
    for date, rolls in data.items():
        # Create a row for each roll under the given date
        for roll in rolls:
            table_data.append({'Date': date, 'Roll': roll})

    # Create a DataFrame from the table data
    df = pd.DataFrame(table_data)
    return df


# Main Streamlit app function
def main():
    # File name of the JSON file
    filename = 'rolls.json'

    # Load the JSON data
    data = load_json_file(filename)

    if data:
        # Convert JSON data to a table format
        df = json_to_table(data)

        # Display the DataFrame as a table
        st.table(df)

        # Optionally, you can display the raw JSON data as well
        st.json(data)


if __name__ == '__main__':
    main()

