import matplotlib.pyplot as plt
import numpy as np

def make_scatter(df, theta_list):
    # plt.scatter(df["km"], df["price"])
    # plt.title('Km vs Price')
    # plt.xlabel('Km')
    # plt.ylabel('Price')
    # plt.savefig("pricedata1.png")

    # plt.scatter(df["km_normalized"], df["price_normalized"])
    # plt.title('Km vs Price')
    # plt.xlabel('Km')
    # plt.ylabel('Price')
    # plt.savefig("pricedata2.png")
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    ax1.scatter(df["km"], df["price"])
    ax1.set_title('Km vs Price (Original)')
    ax1.set_xlabel('Km')
    ax1.set_ylabel('Price')
    x1 = np.linspace(df['km'].min(), df['km'].max(), 100)
    y = x1 * theta_list["theta1"] + theta_list["theta0"]
    ax1.plot(x1, y)


    ax2.scatter(df["km_normalized"], df["price_normalized"])
    ax2.set_title('Km vs Price (Normalized)')
    ax2.set_xlabel('Km (Normalized)')
    ax2.set_ylabel('Price (Normalized)')
    x2 = np.linspace(0, 1, 100)
    y = x2 * theta_list["theta1_normalized"] + theta_list["theta0_normalized"]
    ax2.plot(x2, y)

    plt.tight_layout()
    plt.savefig("combined_price_data.png")
    plt.close()

def make_precision(precision_list):

    plt.plot(precision_list)
    plt.title("MSE vs The number of times")
    plt.xlabel('The number of times')
    plt.ylabel('MSE')
    # plt.xscale('log')
    plt.savefig("precision.png")
