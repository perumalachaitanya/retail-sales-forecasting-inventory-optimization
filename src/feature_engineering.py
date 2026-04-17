def create_features(df):
    df = df.sort_values(["store_id", "item_id", "date"])

    df["lag_1"] = df.groupby(["store_id", "item_id"])["qty_sold"].shift(1)
    df["lag_7"] = df.groupby(["store_id", "item_id"])["qty_sold"].shift(7)

    df["rolling_mean"] = df.groupby(["store_id", "item_id"])["qty_sold"].shift(1).rolling(7).mean()

    df = df.dropna()

    return df