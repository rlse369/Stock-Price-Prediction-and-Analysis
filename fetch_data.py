# Import Required Libraries
# Install
# pip install pandas yfinance matplotlib seaborn
# Import
import yfinance as yf
import pandas as pd
import os
print(os.getcwd())  

# Define the stock ticker symbol
ticker = "AAPL" #Exp:Apple

# Fetch the stock data
apple = yf.Ticker(ticker)

# Get historical market data
df = apple.history(period="5y")

# Fetch fundamental data
financials = apple.financials
balance_sheet = apple.balance_sheet
cashflow = apple.cashflow

# Print key financial metrics
print("Revenue:", financials.loc["Total Revenue"].iloc[0])
print("Net Income:", financials.loc["Net Income"].iloc[0])
print("EPS:", financials.loc["Diluted EPS"].iloc[0])

# Save to CSV for analysis
df.to_csv("apple_stock_data.csv", index=False)

print("Apple stock data saved successfully!")