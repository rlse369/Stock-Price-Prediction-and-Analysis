#pip install yfinance (terminal)
import yfinance as yf
import os

#Define the stock ticker symbol
ticker = "AAPL" #Exp:Apple

#Fetch the stock data
stock_data = yf.Ticker(ticker)

#Get historical market data
historical_data = stock_data.history(period="1y") 

#Display the data
print(historical_data.head())

#Customize the date range
historical_data = stock_data.history(start="2024-01-01", end="2024-12-31")
print(historical_data.head())

# Ensure the directory exists before saving
os.makedirs("rlse369", exist_ok=True)

# Save dataset as CSV
file_path = "rlse369/Stock-Price-Prediction-and-Analysis.csv"
historical_data.to_csv(file_path)

# Check if the file was saved successfully
print(os.path.exists(file_path))  # Should print True if successful