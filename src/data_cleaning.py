import pandas as pd

def load_data():

    df = pd.read_csv("data/nassau_candy.csv")

    df.columns = df.columns.str.strip()

    return df