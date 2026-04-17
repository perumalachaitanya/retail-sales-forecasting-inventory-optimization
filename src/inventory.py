import numpy as np

def calculate_inventory(df):
    results = []

    for (store, item), group in df.groupby(["store_id", "item_id"]):
        avg_demand = group["prediction"].mean()
        std_demand = group["prediction"].std()

        lead_time = 7
        service_level = 1.65  # 95%

        safety_stock = service_level * std_demand * np.sqrt(lead_time)
        reorder_point = (avg_demand * lead_time) + safety_stock

        results.append({
            "store_id": store,
            "item_id": item,
            "avg_demand": avg_demand,
            "safety_stock": safety_stock,
            "reorder_point": reorder_point
        })

    return results