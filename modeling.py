import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
from config import PROCESSED_DATA_FILE, LSTM_MODEL_FILE, MODEL_DIR
import os

def prepare_data():
    """Prepare stock data for LSTM model training"""
    data = pd.read_csv(PROCESSED_DATA_FILE)
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)

    # Select the feature and normalize it
    scaler = MinMaxScaler()
    data['Close Prices'] = scaler.fit_transform(data[['Close Prices']])

    # Create sequences for LSTM input
    sequence_length = 50
    X, y = [], []
    for i in range(len(data) - sequence_length):
        X.append(data['Close Prices'].values[i:i+sequence_length])
        y.append(data['Close Prices'].values[i+sequence_length])

    X, y = np.array(X), np.array(y)

    # Reshape for LSTM
    X = X.reshape((X.shape[0], X.shape[1], 1))

    return X, y, scaler

def build_lstm_model():
    """Build and compile LSTM model"""
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=(50, 1)),
        Dropout(0.2),
        LSTM(50, return_sequences=False),
        Dropout(0.2),
        Dense(1)
    ])

    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def train_model():
    """Train LSTM model and save it"""
    X, y, scaler = prepare_data()

    model = build_lstm_model()

    model.fit(X, y, epochs=20, batch_size=16, validation_split=0.1)

    # Ensure model directory exists
    os.makedirs(MODEL_DIR, exist_ok=True)

    # Save the trained model
    model.save(LSTM_MODEL_FILE)
    print(f"Model saved at {LSTM_MODEL_FILE}")

if __name__ == "__main__":
    train_model()
