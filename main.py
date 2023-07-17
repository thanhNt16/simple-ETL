import pandas as pd

df = pd.read_csv("exchange_rates.csv")
print(df.head(5))

# df = df[df["country"] == "GBP"]
# print(df)
