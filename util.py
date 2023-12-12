import pandas as pd

def get_data(PATH):
    df = pd.read_csv(PATH)
    df["Date"] = pd.to_datetime(df["Date"])
    return df