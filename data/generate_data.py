import pandas as pd
import numpy as np

dates = pd.date_range(start='2023-01-01', periods=365)

sales = np.random.poisson(lam=20, size=365)

# Add trend + seasonality
trend = np.linspace(0, 10, 365)
seasonality = 5 * np.sin(np.linspace(0, 20, 365))

sales = sales + trend + seasonality
sales = sales.astype(int)

df = pd.DataFrame({
    'date': dates,
    'sales': sales
})

df.to_csv('data/retail_data.csv', index=False)

print("Dataset created!")