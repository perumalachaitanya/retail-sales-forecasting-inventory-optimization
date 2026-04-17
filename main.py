from src.data_preprocessing import load_data
from src.feature_engineering import create_features
from src.model import train_model
from src.forecast import forecast
from src.inventory import calculate_inventory

def main():
    print("Loading data...")
    df = load_data()

    print("Creating features...")
    df = create_features(df)

    print("Training model...")
    model = train_model(df)

    print("Generating forecast...")
    df = forecast(df)

    print("Calculating inventory...")
    inventory = calculate_inventory(df)

    print("\nInventory Recommendations:\n")
    for item in inventory:
        print(item)

if __name__ == "__main__":
    main()