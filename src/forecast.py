import joblib

def forecast(df):
    model = joblib.load("models/model.pkl")

    features = ["store_id", "item_id", "lag_1", "lag_7", "rolling_mean"]
    
    X = df[features]
    df["prediction"] = model.predict(X)

    return df