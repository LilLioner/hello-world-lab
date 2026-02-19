'''Soma seletiva

Some apenas os números pares de uma lista:

numeros = [3, 10, 7, 18, 5, 22, 9]


 Esperado: 10 + 18 + 22 = 50'''

numeros = [3, 10, 7, 18, 5, 22, 9]
soma = 0
for numero in numeros:
  if numero % 2 == 0:
    soma += numero
print("Soma dos pares = ", soma)

'''
 Intercalando listas (zip + loop)

Dadas duas listas:

nomes = ["Ana", "Carlos", "Joao"]
idades = [20, 35, 17]


Crie frases assim:

Ana tem 20 anos
Carlos tem 35 anos
Joao tem 17 anos


 Depois tente fazer sem zip também.'''

nomes = ["Ana", "Carlos", "Joao"]
idades = [20, 35, 17]

for nome, idade in zip(nomes, idades):
  print(nome, "tem", idade, "anos") #achei fácil 👽

#Agora sem o zip...   

for i in range(len(nomes)):
  print(nomes[i], "tem", idades[i], "anos")

  '''Você tem duas listas:

alunos = ["Lucas", "Marina", "Pedro", "Julia"]
notas = [7.5, 9.0, 5.8, 6.5]


 Mostre:

Lucas: Aprovado
Marina: Aprovado
Pedro: Reprovado
Julia: Aprovado


Regra:

nota ≥ 6 → aprovado

nota < 6 → reprovado

 Faça sem zip.'''
  
alunos = ["Lucas", "Marina", "Pedro", "Julia"]
notas = [7.5, 9.0, 5.8, 6.5]

for x in range(len(alunos)):
  if notas[x] >= 6 :
    print(alunos[x],":", "Aprovado com nota ", notas[x])
  else:
    print(alunos[x],":", "Reprovado com nota", notas[x])

'''Conte quantas consoantes existem numa string:

frase = "Python eh muito poderoso"

 Ignore maiúsculas/minúsculas.'''

frase = "Python eh muito poderoso"
vogais = 0

for vogal in frase.lower():
  if vogal == "a" or vogal == "e" or vogal =="i"or vogal =="o" or vogal =="u":
    continue
  else:
    vogais += 1
print(vogais)