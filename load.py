import pandas as pd

def load_csv(path: str):
    df = pd.read_csv(path)
    # print(df)
    return df