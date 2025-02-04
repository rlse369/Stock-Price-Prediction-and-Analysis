import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from config import RAW_DATA_FILE

# Load stock data
def load_data():
    data = pd.read_csv(RAW_DATA_FILE)
    data['Date'] = pd.to_datetime(data['Date'])  # Convert to datetime
    return data

# Plot Closing Prices Over Time
def plot_closing_prices(data):
    plt.figure(figsize=(12,6))
    plt.plot(data['Date'], data['Close Prices'], label="Closing Price", color="blue")
    plt.title("Apple (AAPL) Closing Prices Over Time", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Closing Price (USD)", fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()

# Plot Trading Volume
def plot_trading_volume(data):
    plt.figure(figsize=(12,6))
    plt.plot(data['Date'], data['Trading Volume'], label="Trading Volume", color="orange")
    plt.title("Apple (AAPL) Trading Volume Over Time", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Trading Volume", fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()

# Correlation Between Trading Volume and Closing Prices
def plot_correlation(data):
    correlation = data[['Trading Volume', 'Close Prices']].corr()
    print("Correlation between Trading Volume and Close Price:\n", correlation)
    
    sns.jointplot(data=data, x="Trading Volume", y="Close Prices", kind="scatter", height=8)
    plt.show()

# Calculate and Plot Moving Averages
def plot_moving_averages(data):
    data['50_MA'] = data['Close Prices'].rolling(window=50).mean()
    data['200_MA'] = data['Close Prices'].rolling(window=200).mean()

    plt.figure(figsize=(12,6))
    plt.plot(data['Date'], data['Close Prices'], label="Closing Price", color="blue", alpha=0.5)
    plt.plot(data['Date'], data['50_MA'], label="50-Day Moving Average", color="green")
    plt.plot(data['Date'], data['200_MA'], label="200-Day Moving Average", color="red")
    plt.title("Apple (AAPL) Stock with Moving Averages", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Price (USD)", fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()

# Run all EDA steps
def run_eda():
    data = load_data()
    plot_closing_prices(data)
    plot_trading_volume(data)
    plot_correlation(data)
    plot_moving_averages(data)

if __name__ == "__main__":
    run_eda()
