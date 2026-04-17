def create_features(df):
    df = df.sort_values('date')
    
    df['day'] = df['date'].dt.dayofweek
    df['lag_1'] = df['sales'].shift(1)
    df['rolling_mean'] = df['sales'].rolling(7).mean()
    
    df = df.dropna()
    return df