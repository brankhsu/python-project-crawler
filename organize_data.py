import numpy as np

#傳入dataFrame會進行統計量的計算
def describe_data(df):
    print("------------------------------已售出數量(數量、平均、標準差、最小、25%、50%、75%、最大值)---------------------------------");
    print(df['已售出數量'].describe())
    print("------------------------------價格(數量、平均、標準差、最小、25%、50%、75%、最大值)---------------------------------");
    print(df['價格'].describe())

#價格的離群值刪除整列；出售數列的離群值也是刪除整列
def remove_outliers(df):
    n = 1.5
    IQR = np.percentile(df['已售出數量'], 75) - np.percentile(df['已售出數量'], 25)
    print(np.percentile(df['已售出數量'], 75))
    df = df[df['已售出數量'] < np.percentile(df['已售出數量'], 75) + n * IQR]
    df = df[df['已售出數量'] > np.percentile(df['已售出數量'], 25) - n * IQR]
    n = 1.5
    IQR = np.percentile(df['價格'], 75) - np.percentile(df['價格'], 25)
    df = df[df['價格'] < np.percentile(df['價格'], 75) + n * IQR]
    df = df[df['價格'] > np.percentile(df['價格'], 25) - n * IQR]
    return df
#移除出售數量掛0的資料
def remove_zero(df):
    indexNames = df[df['已售出數量'] == 0].index
    df.drop(indexNames, inplace=True)
    return df