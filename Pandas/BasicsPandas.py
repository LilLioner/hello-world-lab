from pathlib import Path
import pandas as pd 
base = Path(__file__).parent

####################################



df = { 
  "nome" : ["Ana", "João", "Maria"], 
  "idade" : [25, 30, 28], 
  "salario" : [3000, 5000, 4000] 
  } 

df = pd.DataFrame(df)

print(df[(df["idade"] > 28) & (df["salario"] > 3500)]) #FILTRANDO DATA FRAMES
print(df["salario"].describe())


print(df.head(2)) 
print()
print()
print()

print(df.loc[df["idade"] > 25, ["nome","salario"]])

####################################

var = pd.read_csv(base / "data.csv")


