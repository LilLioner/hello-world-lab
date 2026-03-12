from pathlib import Path
import pandas as pd 

base = Path(__file__).parent

df = pd.read_csv(base / "data.csv")

print(df)
print(df.head())
print(df.info())
print(df.describe())