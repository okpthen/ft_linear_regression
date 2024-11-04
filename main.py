from load import load_csv
from make_scatter import make_scatter, make_precision
from learning import new_thepa
import numpy as np

def estimatePrice(km, theta0, theta1):
    return theta0 + (theta1 * km)

def normalize(df):
    price_min = df['price'].min()
    price_max = df['price'].max()
    df['price_normalized'] = (df['price'] - price_min) / (price_max - price_min)
    km_min = df['km'].min()
    km_max = df['km'].max()
    df['km_normalized'] = (df['km'] - km_min) / (km_max - km_min)

    return df


def main():
    try:
        df = load_csv("data.csv")
    except Exception as e:
        print(e)
        exit(0)
    df = normalize(df)

    theta0 = 0.0
    theta1 = 0.0
    precision = [] #リスト
    theta_list = {} #辞書
    while True:
        new_theta0, new_theta1, precision = new_thepa(theta0, theta1, df, precision)        
        # print(theta0, theta1)
        if new_theta0 == theta0 and new_theta1 == theta1:
            break
        # if new_theta0 >= 0.9999999 *theta1 and 1.0000001 * theta0 >= new_theta0:
        #     break
        theta0 = new_theta0
        theta1 = new_theta1
    
    min_price = df['price'].min()
    max_price = df['price'].max()
    min_km = df['km'].min()
    max_km = df['km'].max()

    theta1_scale = theta1 * (max_price - min_price) / (max_km - min_km)
    theta0_scale = theta0 * (max_price - min_price) + min_price - (theta1_scale * min_km) 
    print(theta0, theta1)
    print(theta0_scale, theta1_scale)

    theta_list["theta0"] = theta0_scale
    theta_list["theta1"] = theta1_scale
    theta_list["theta0_normalized"] = theta0
    theta_list["theta1_normalized"] = theta1

    make_scatter(df, theta_list)
    print(len(precision))
    make_precision(precision)



if __name__ == "__main__":
    main()

# 0.9393189294497382 -1.0035757423969949
# 8499.599649933165 -0.021448963591701817
