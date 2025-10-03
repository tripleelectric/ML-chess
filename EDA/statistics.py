import pandas as pd
import numpy as np

df = pd.read_csv("data/games.csv")

df["rating_diff"] = df["white_rating"] - df["black_rating"]
df["white_wins"] = (df["winner"] == "white").astype(int)

max_rating = df[["white_rating", "black_rating"]].max().max()
min_rating = df[["white_rating", "black_rating"]].min().min()
print((min_rating, max_rating))
