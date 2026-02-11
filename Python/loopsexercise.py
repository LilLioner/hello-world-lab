'''Use um for para imprimir os números de 1 a 10.'''

for i in range(1, 11):
  print(i)


'''Use um for para imprimir apenas os números pares de 0 a 20.'''

for j in range(0, 20, 2):
  print(j)

'''Use um for para imprimir cada letra da palavra "python" em uma linha.'''

for letra in "Python":
  print(letra)

  '''Dada a lista:

cores = ["vermelho", "azul", "verde", "amarelo"]


Imprima o índice e a cor, usando enumerate.'''

cores = ["vermelho", "azul", "verde", "amarelo"]

for indice, cor in enumerate(cores):
  print(indice, cor)

'''Imprima os números de 0 a 9, mas pule o número 5 usando continue.''' 

for n in range(10):
  if n == 5:
    continue
  print(n)

'''Imprima os números de 0 a 9, mas pare o loop quando chegar no 7, usando break.'''

for m in range(10):
  if m == 7:
    break
  print(m)  

'''Use um while para imprimir os números de 1 a 5.'''

contagem = 1
while contagem <= 5:
  print(contagem)
  contagem += 1

''' Juntando listas

Dadas as listas:

nomes = ["Ana", "Bruno", "Carlos"]
idades = [20, 25, 30]


Imprima:

Ana tem 20 anos
Bruno tem 25 anos
Carlos tem 30 anos


(usando zip)'''

nomes = ["Ana", "Bruno", "Carlos"]
idades = [20, 25, 30]

for f, (nome, idade) in enumerate(zip(nomes, idades), start=1):
  print(f, nome, "tem", idade, "anos")

''' Índice + duas listas
Usando as mesmas listas acima, imprima também o índice da pessoa (começando em 1).'''

'''Tabela simples

Use loops aninhados para imprimir:

1 1
1 2
1 3
2 1
2 2
2 3'''

for lista in range(1, 3):
  for lista2 in range(1, 4):
    print(lista, lista2)


'''Tabuada

Imprima a tabuada do 1 ao 3, usando loops aninhados.'''

for numero_mtp in range(1, 4):
  for multiplica in range (1, 4):
    print(numero_mtp, " x ", multiplica, "=" ,numero_mtp*multiplica)

'''Dada a matriz:

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]


Imprima todos os números, um por linha, usando loops aninhados.'''

matriz = [
    [1, 2, 3]
    [4, 5, 6]
]

