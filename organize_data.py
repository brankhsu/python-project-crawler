import numpy as np

def describe_data(df):
    print("------------------------------已售出數量(數量、平均、標準差、最小、25%、50%、75%、最大值)---------------------------------");
    print(df['已售出數量'].describe())
    print("------------------------------價格(數量、平均、標準差、最小、25%、50%、75%、最大值)---------------------------------");
    print(df['價格'].describe())

def remove_outliers(df):
    n = 1.5
    IQR = np.percentile(df['已售出數量'], 75) - np.percentile(df['已售出數量'], 25)
    df = df[df['已售出數量'] < np.percentile(df['已售出數量'], 75) + n * IQR]
    df = df[df['已售出數量'] > np.percentile(df['已售出數量'], 25) - n * IQR]
    n = 1.5
    IQR = np.percentile(df['價格'], 75) - np.percentile(df['價格'], 25)
    df = df[df['價格'] < np.percentile(df['價格'], 75) + n * IQR]
    df = df[df['價格'] > np.percentile(df['價格'], 25) - n * IQR]
    return df

def remove_zero(df):
    indexNames = df[df['已售出數量'] == 0].index
    df.drop(indexNames, inplace=True)
    return df