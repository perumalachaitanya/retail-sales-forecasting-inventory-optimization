from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def train_model(df):
    features = ["store_id", "item_id", "lag_1", "lag_7", "rolling_mean"]
    
    X = df[features]
    y = df["qty_sold"]

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    # ✅ Ensure models folder exists
    os.makedirs("models", exist_ok=True)

    joblib.dump(model, "models/model.pkl")

    return model