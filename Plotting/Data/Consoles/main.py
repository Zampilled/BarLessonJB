import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("./dataset.csv")
    print(df.head())
    df.drop(["name", "year_of_release", "publisher", "na_sales", "eu_sales", "jp_sales", "other_sales", "global_sales",
             "critic_score", "critic_count", "user_score", "user_count", "developer", "rating"
             ], axis=1, inplace=True)

    print(df.head())
