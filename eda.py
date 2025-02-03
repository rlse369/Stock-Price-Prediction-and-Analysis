import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
selected_columns = pd.read_csv("C:/Users/rache/Downloads/apple_stock_data.csv")

# Exploratory Data Analysis(EDA)
# Plot Closing Prices Over Time
# To identify trends and seasonality
plt.figure(figsize=(12,6))
plt.plot(selected_columns['Date'], selected_columns['Close Prices'], label="Closing Price", color="blue")
plt.title("Apple (APPL) Closing Prices Over Time in Year 2024", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Closing Price (USD)", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

# Analyse Trading Volume and Its Correlation with Price Changes
# Plot Trading Volume
plt.figure(figsize=(12,6))
plt.plot(selected_columns['Date'], selected_columns['Trading Volume'], label="Trading Volume", color="orange")
plt.title("Apple (APPL) Trading Volume Over Time in Year 2024", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Trading Volume", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
# Correlation Between Trading Volume and Price
# Calculate correlation
correlation = selected_columns[['Trading Volume', 'Close Prices']].corr()
print("Correlation between Trading Volume and Close Price:")
print(correlation)
# Visualise the correlation
sns.jointplot(data=selected_columns, x="Trading Volume", y="Close Prices", kind="scatter", height=8)
plt.show()

# Calculate and Plot Moving Averages
# Calculate Moving Averages
selected_columns['50_MA'] = selected_columns['Close Prices'].rolling(window=50).mean()
selected_columns['200_MA'] = selected_columns['Close Prices'].rolling(window=200).mean()
# Plot Moving Averages:
plt.figure(figsize=(12,6))
plt.plot(selected_columns['Date'], selected_columns['Close Prices'], label="Closing Price", color="blue", alpha=0.5)
plt.plot(selected_columns['Date'], selected_columns['50_MA'], label="50-Day Moving Average", color="green")
plt.plot(selected_columns['Date'], selected_columns['200_MA'], label="200-Day Moving Average", color="red")
plt.title("Apple (APPL) Stock with 50-Day and 200-Day Moving Averages", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Price (USD)", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()