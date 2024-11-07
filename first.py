import pandas as pd
from learning import estimatePrice


def load_csv(path: str):
    df = pd.read_csv(path)
    return df

def main():
    try:
        df = load_csv("data.csv")
    except Exception as e:
        print(e)
        exit(0)
    try:
        theta = pd.read_csv("train_data.csv", index_col=0)
    except FileNotFoundError:
        theta = pd.DataFrame([0, 0], index=["theta0", "theta1"], columns=["value"])
    theta0 = theta.loc["theta0", "value"]
    theta1 = theta.loc["theta1", "value"]
    for index in range(len(df)):
        km_value = df["km"][index]
        estimated_price = estimatePrice(df["km"][index], theta0, theta1)
        real_price = df["price"][index]
        print(f"km = {km_value}\testimateprice = {estimated_price}\tprice = {real_price}")


if __name__ == "__main__":
    main()