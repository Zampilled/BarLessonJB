import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":
    # Inputs data into dataframe
    df = pd.read_csv("./dataset.csv")

    # Drops unneeded columns
    df.drop(["name", "year_of_release", "publisher", "na_sales", "eu_sales", "jp_sales", "other_sales", "global_sales",
             "critic_score", "critic_count", "user_score", "user_count", "developer", "rating"
             ], axis=1, inplace=True)

    # Keeps only the 4 needed consoles
    consoles = ["PS4", "XOne", "PC", "WiiU"]
    df=df[df['platform'].isin(consoles)]

    # Plots Graph
    sns.countplot(x='platform', hue='genre', data=df)

