# Import Required Libraries
# Install
# pip install pandas yfinance matplotlib seaborn
# Import
import yfinance as yf
import pandas as pd

# Define the stock ticker symbol
ticker = "AAPL" #Exp:Apple

# Fetch the stock data
apple_stock_data = yf.Ticker(ticker)

# Get historical market data
history_data = apple_stock_data.history(period="1y")

# Customise date range
historical_data = apple_stock_data.history(start="2024-01-01", end="2024-12-31")

# Reset index to access 'Date' as a column
historical_data.reset_index(inplace=True)

# Convert 'Date' to datetime and remove time and timezone
historical_data['Date'] = pd.to_datetime(historical_data['Date']).dt.strftime('%Y-%m-%d')

# Select only the required columns and rename
selected_columns = historical_data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
selected_columns = selected_columns.rename(columns={'Open': 'Open Prices', 'Close': 'Close Prices', 'Volume': 'Trading Volume'})

# Save to CSV for analysis
selected_columns.to_csv("C:/Users/rache/Downloads/apple_stock_data.csv", index=False)

print("Apple stock data saved successfully!")
