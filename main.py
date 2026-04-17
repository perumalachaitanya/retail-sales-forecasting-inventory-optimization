from src.data_preprocessing import load_data, clean_data
from src.feature_engineering import create_features
from src.model import train_model
from src.inventory import inventory_calc
import pandas as pd

# Load data
df = load_data()
df = clean_data(df)

# Features
df = create_features(df)

# Model
X = df[['lag_1', 'rolling_mean', 'day']]
y = df['sales']

model = train_model(X, y)

# Forecast
forecast = model.predict(X)

# Inventory
ss, rop = inventory_calc(forecast)

print("Safety Stock:", ss)
print("Reorder Point:", rop)

import pandas as pd

# Save forecast output
forecast_df = pd.DataFrame({
    'actual_sales': y,
    'predicted_sales': forecast
})

forecast_df.to_csv('outputs/forecast.csv', index=False)

# Save inventory output
inventory_df = pd.DataFrame({
    'safety_stock': [ss],
    'reorder_point': [rop]
})

inventory_df.to_csv('outputs/inventory.csv', index=False)

# Save outputs
pd.DataFrame({
    'actual': y,
    'predicted': forecast
}).to_csv('outputs/forecast.csv', index=False)

import matplotlib.pyplot as plt

plt.plot(y.values, label='Actual')
plt.plot(forecast, label='Predicted')
plt.legend()
plt.savefig('images/forecast.png')
plt.show()

import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
plt.plot(df['date'], df['sales'])
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.savefig('images/sales_trend.png')
plt.show()

plt.figure(figsize=(10,5))
plt.plot(y.values, label='Actual Sales')
plt.plot(forecast, label='Predicted Sales')
plt.legend()
plt.title("Actual vs Predicted Sales")
plt.savefig('images/forecast_vs_actual.png')
plt.show()