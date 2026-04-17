import pandas as pd
import os

def load_data():
    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_path, "data", "retail_data.csv")

    df = pd.read_csv(file_path, parse_dates=["date"])
    return df