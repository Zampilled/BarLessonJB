import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("./dataset.csv")

    df.drop(["name", "year_of_release", "publisher", "na_sales", "eu_sales", "jp_sales", "other_sales", "global_sales",
             "critic_score", "critic_count", "user_score", "user_count", "developer", "rating"
             ], axis=1, inplace=True)


    consoles = ["PS4", "XOne", "PC", "WiiU"]
    df=df[df['platform'].isin(consoles)]
