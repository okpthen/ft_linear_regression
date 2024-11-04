from config import LearningRate

def estimatePrice(km, theta0, theta1):
    return theta0 + (theta1 * km)


def new_thepa(theta0: float, theta1: float, df, precision_list: list):
    m = len(df)
    sum_thepa0 = sum(estimatePrice(df['km_normalized'][i], theta0, theta1) - df['price_normalized'][i] for i in range(m))
    sum_thepa1 = sum((estimatePrice(df['km_normalized'][i], theta0, theta1) - df['price_normalized'][i]) * df['km_normalized'][i] for i in range(m))
    precision = sum((estimatePrice(df['km_normalized'][i], theta0, theta1) - df['price_normalized'][i]) ** 2 for i in range(m))
    precision_list.append(precision / m)
    theta0 -= (LearningRate * sum_thepa0 / m)
    theta1 -= (LearningRate * sum_thepa1 / m)
    return theta0, theta1, precision_list
