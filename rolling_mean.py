def filter(df):
    return df.rolling(10).mean(center=False)