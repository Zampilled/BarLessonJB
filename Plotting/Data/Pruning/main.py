import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("./dataset.csv")
    print(df.head())

