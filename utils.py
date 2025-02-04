import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from config import PROCESSED_DATA_FILE

def load_data():
    """Load the processed stock data"""
    return pd.read_csv(PROCESSED_DATA_FILE)

def plot_stock_prices(data):
    """Plot closing prices over time"""
    plt.figure(figsize=(12,6))
    plt.plot(data['Date'], data['Close Prices'], label="Closing Price", color="blue")
    plt.title("Apple (AAPL) Closing Prices Over Time", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Closing Price (USD)", fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_correlation(data):
    """Plot correlation between Trading Volume and Closing Prices"""
    correlation = data[['Trading Volume', 'Close Prices']].corr()
    print("Correlation between Trading Volume and Close Price:")
    print(correlation)

    sns.jointplot(data=data, x="Trading Volume", y="Close Prices", kind="scatter", height=8)
    plt.show()
