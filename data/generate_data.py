import pandas as pd
import numpy as np

np.random.seed(42)

dates = pd.date_range(start="2023-01-01", periods=365)

data = []

stores = [1, 2]
items = [101, 102, 103]  # 3 products

for store in stores:
    for item in items:
        base = np.random.randint(20, 50)
        for date in dates:
            demand = base + np.random.randint(-10, 10)
            demand = max(0, demand)

            data.append([store, item, date, demand])

df = pd.DataFrame(data, columns=["store_id", "item_id", "date", "qty_sold"])

df.to_csv("data/retail_data.csv", index=False)
print("Dataset created!")