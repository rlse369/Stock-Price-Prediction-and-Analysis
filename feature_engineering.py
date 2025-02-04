import pandas as pd
from config import PROCESSED_DATA_FILE

def create_features():
    """Generate lag features and technical indicators"""
    data = pd.read_csv(PROCESSED_DATA_FILE)
    data['Date'] = pd.to_datetime(data['Date'])
    
    # Create lag features (previous day's prices)
    data['Close_Lag_1'] = data['Close Prices'].shift(1)
    data['Close_Lag_2'] = data['Close Prices'].shift(2)
    
    # Moving Averages
    data['50_MA'] = data['Close Prices'].rolling(window=50).mean()
    data['200_MA'] = data['Close Prices'].rolling(window=200).mean()

    # Relative Strength Index (RSI)
    delta = data['Close Prices'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))

    # Drop rows with NaN values due to feature calculations
    data.dropna(inplace=True)

    # Save the enhanced dataset
    data.to_csv(PROCESSED_DATA_FILE, index=False)
    print("Feature engineering completed and saved!")

if __name__ == "__main__":
    create_features()
