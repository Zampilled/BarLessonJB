import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":
    # Inputs data into dataframe
    df = pd.read_csv("./dataset.csv")
    print(df.head())

