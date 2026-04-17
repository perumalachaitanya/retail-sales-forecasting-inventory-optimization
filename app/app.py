import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import joblib
import numpy as np

from src.data_preprocessing import load_data
from src.feature_engineering import create_features
from src.inventory import calculate_inventory

st.title("📊 Retail Forecasting & Inventory Optimization")

# Load data
df = load_data()
df = create_features(df)

# Load model
model = joblib.load("models/model.pkl")

# Dropdowns
store_ids = df["store_id"].unique()
item_ids = df["item_id"].unique()

store = st.selectbox("Select Store", store_ids)
item = st.selectbox("Select Product (Item)", item_ids)

# Filter data
filtered_df = df[(df["store_id"] == store) & (df["item_id"] == item)]

# Input
on_hand = st.number_input("Current Stock", min_value=0, value=100)

# Predict
if st.button("Generate Forecast & Recommendation"):

    features = ["store_id", "item_id", "lag_1", "lag_7", "rolling_mean"]

    X = filtered_df[features]
    filtered_df["prediction"] = model.predict(X)

    st.subheader("📈 Forecast")
    st.line_chart(filtered_df.set_index("date")[["qty_sold", "prediction"]])

    # Inventory calculation
    avg_demand = filtered_df["prediction"].mean()
    std_demand = filtered_df["prediction"].std()

    lead_time = 7
    service_level = 1.65

    safety_stock = service_level * std_demand * np.sqrt(lead_time)
    reorder_point = (avg_demand * lead_time) + safety_stock

    st.subheader("📦 Inventory Insights")
    st.write(f"Average Demand: {avg_demand:.2f}")
    st.write(f"Safety Stock: {safety_stock:.2f}")
    st.write(f"Reorder Point: {reorder_point:.2f}")

    if on_hand < reorder_point:
        st.error("⚠️ Stock is LOW! Place order immediately.")
    else:
        st.success("✅ Stock level is sufficient.")