import numpy as np
import pandas as pd
from datetime import datetime

def calculate_days_elapsed(input_date_str, compare_date=None):
    """
    calculates the number of days between an input date and a comparison date.
    if no comparison date is provided, it defaults to 'today'.
    """
    # use numpy datetime64 for the input
    try:
        start = np.datetime64(input_date_str)
    except ValueError:
        return "error: invalid date format. please use yyyy-mm-dd"

    # determine the end date (today or a custom date for testing)
    if compare_date:
        end = np.datetime64(compare_date)
    else:
        end = np.datetime64('today')

    # calculate the difference
    delta = end - start
    
    # return as an integer (number of days)
    return delta.astype('timedelta64[D]').astype(int)

def process_csv_dates(filepath):
    """
    loads a csv file and calculates the age of every date in the column.
    """
    try:
        df = pd.read_csv(filepath)
        print(f"loaded {len(df)} dates from {filepath}")
        
        # apply the calculation to the whole column
        results = []
        for date_str in df['date']:
            days = calculate_days_elapsed(date_str)
            results.append(days)
            print(f"date: {date_str} was {days} days ago")
            
        return results
        
    except FileNotFoundError:
        print("error: csv file not found.")
        return []

if __name__ == "__main__":
    # 1. user input section
    print("--- manual date calculator ---")
    user_date = input("enter a date (yyyy-mm-dd): ")
    days_ago = calculate_days_elapsed(user_date)
    print(f"that date was {days_ago} days ago.\n")

    # 2. csv processing section
    print("--- csv batch processing ---")
    process_csv_dates("random_dates.csv")