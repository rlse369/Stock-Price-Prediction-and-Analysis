import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from config import PROCESSED_DATA_FILE

def analyze_trends():
    """Decompose and visualize stock price trends and seasonality"""
    data = pd.read_csv(PROCESSED_DATA_FILE)
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)

    # Decompose the time series into trend, seasonality, and residuals
    decomposition = sm.tsa.seasonal_decompose(data['Close Prices'], model='additive', period=30)

    # Plot decomposition
    plt.figure(figsize=(12,8))
    decomposition.plot()
    plt.show()

def plot_autocorrelations():
    """Plot Autocorrelation and Partial Autocorrelation"""
    data = pd.read_csv(PROCESSED_DATA_FILE)
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)

    plt.figure(figsize=(12,6))
    plot_acf(data['Close Prices'], lags=30)
    plt.show()

    plt.figure(figsize=(12,6))
    plot_pacf(data['Close Prices'], lags=30)
    plt.show()

def run_time_series_analysis():
    analyze_trends()
    plot_autocorrelations()

if __name__ == "__main__":
    run_time_series_analysis()
