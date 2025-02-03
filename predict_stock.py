import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load data
df = pd.read_csv("C:/Users/rache/Downloads/apple_stock_data.csv", usecols=["Date", "Close"], parse_dates=["Date"], index_col="Date")

# Scale data
scaler = MinMaxScaler(feature_range=(0,1))
df["Close"] = scaler.fit_transform(df["Close"].values.reshape(-1,1))

# Prepare training data
train_size = int(len(df) * 0.8)
train_data, test_data = df[:train_size], df[train_size:]

def create_dataset(data, time_step=60):
    X, Y = [], []
    for i in range(len(data)-time_step-1):
        X.append(data[i:(i+time_step), 0])
        Y.append(data[i+time_step, 0])
    return np.array(X), np.array(Y)

time_step = 60
X_train, Y_train = create_dataset(train_data.values, time_step)
X_test, Y_test = create_dataset(test_data.values, time_step)

# Reshape for LSTM
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

# Build LSTM Model
model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(time_step,1)),
    LSTM(50, return_sequences=False),
    Dense(25),
    Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, Y_train, epochs=10, batch_size=16, validation_data=(X_test, Y_test))

# Predict and visualize
predictions = model.predict(X_test)
predictions = scaler.inverse_transform(predictions)

plt.plot(df.index[-len(predictions):], scaler.inverse_transform(Y_test.reshape(-1,1)), label="Actual")
plt.plot(df.index[-len(predictions):], predictions, label="Predicted")
plt.legend()
plt.show()


