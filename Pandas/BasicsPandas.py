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

print(df)

print(df["salario"].describe())



print(df[(df["idade"] > 28) & (df["salario"] > 3500)]) #FILTRANDO DATA FRAMES
print(df["salario"].describe())


print()
print()
print()

print(df.loc[df["idade"] > 25, ["nome","salario"]])

####################################
#inspeção
'''
print(df.head(2))  
print(df.tail(2))  
print(df.sample(2)) # duas linhas aleatorias  

print(df.shape) 
print(df.columns) 

print(df.info())
print(df.describe())
'''
#####################################
#TRATAMENTO DE DADOS

var = pd.read_csv(base / 'vendas_tech.csv')

#tratamento de colunas:
#nesse caso, vamos excluir uma coluna inteira (pois ela possui apenas 1 valor nao nulo dentre milhares.)
var = var.drop(columns="Data_Base") # drop é o comando de exclusao do pandas

# tratamento de valores nulos

print(var.info())

vardropna = var.dropna() # dropna exlclui qualquer linha que houver pelo menos 1 atributo Nulo
varfillna = var.fillna("Valor") # ao inves de excluir os nulos, ele agora preenche todo o valor nulo no valor desejado.
print(vardropna)


#padronização

df["coluna"] = df["coluna"].str.upper() # padronização por texto, primeiro ele define que o valor é uma string e que todos os valores vao ser em caixa alta. 
#obvio que existem diversas formas diferentes de padronizar um texto, isso é apenas um exemplo.


#duplicatas

df = df.drop_duplicates(subset="Coluna", keep="last")# Exclui todas as linhas aonde a coluna escolhida tenha duplicatas,  o comando keep, determina qual linha duplicada manter, a primeira ou a ultima.