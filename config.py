import os

# Define directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
MODEL_DIR = os.path.join(BASE_DIR, "models")

# Define file paths
RAW_DATA_FILE = os.path.join(DATA_DIR, "raw_stock_data.csv")
PROCESSED_DATA_FILE = os.path.join(DATA_DIR, "processed_stock_data.csv")
LSTM_MODEL_FILE = os.path.join(MODEL_DIR, "lstm_model.h5")

# Stock Ticker
TICKER = "AAPL"  # Apple Stock
START_DATE = "2024-01-01"
END_DATE = "2024-12-31"

# LSTM Model Parameters
SEQUENCE_LENGTH = 50
EPOCHS = 20
BATCH_SIZE = 16
LEARNING_RATE = 0.001

# Ensure directories exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(MODEL_DIR, exist_ok=True)
