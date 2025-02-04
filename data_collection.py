import yfinance as yf
import pandas as pd
import os
from config import RAW_DATA_FILE, TICKER, START_DATE, END_DATE, DATA_DIR

def fetch_stock_data():
    """Fetch Apple stock data and save as CSV"""
    stock = yf.Ticker(TICKER)
    
    # Fetch historical data
    historical_data = stock.history(start=START_DATE, end=END_DATE)

    # Reset index to access 'Date' as a column
    historical_data.reset_index(inplace=True)

    # Convert 'Date' to datetime and remove time component
    historical_data['Date'] = historical_data['Date'].dt.strftime('%Y-%m-%d')

    # Select and rename columns
    selected_columns = historical_data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
    selected_columns = selected_columns.rename(columns={'Open': 'Open Prices', 'Close': 'Close Prices', 'Volume': 'Trading Volume'})

    # Ensure 'data/' directory exists
    os.makedirs(DATA_DIR, exist_ok=True)

    # Save to CSV
    selected_columns.to_csv(RAW_DATA_FILE, index=False)
    print(f"Stock data saved at {RAW_DATA_FILE}")

    return selected_columns  # Return DataFrame for further use

if __name__ == "__main__":
    fetch_stock_data()
