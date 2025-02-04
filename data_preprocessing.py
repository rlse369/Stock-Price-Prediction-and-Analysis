import pandas as pd
import os
from config import RAW_DATA_FILE, PROCESSED_DATA_FILE, DATA_DIR

def preprocess_data():
    """Load, clean, and preprocess stock data"""
    data = pd.read_csv(RAW_DATA_FILE)

    # Convert 'Date' to datetime format
    data['Date'] = pd.to_datetime(data['Date'])

    # Handle missing values (Fill with previous values or drop)
    data.ffill(inplace=True)

    # Normalize numerical features (optional, useful for modeling)
    numerical_cols = ['Open Prices', 'High', 'Low', 'Close Prices', 'Trading Volume']
    data[numerical_cols] = (data[numerical_cols] - data[numerical_cols].min()) / (data[numerical_cols].max() - data[numerical_cols].min())

    # Ensure 'data/' directory exists
    os.makedirs(DATA_DIR, exist_ok=True)

    # Save processed data
    data.to_csv(PROCESSED_DATA_FILE, index=False)
    print(f"Processed data saved at {PROCESSED_DATA_FILE}")

    return data  # Return DataFrame for further use

if __name__ == "__main__":
    preprocess_data()
