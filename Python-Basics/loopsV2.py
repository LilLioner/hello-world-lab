'''frutas = ["Maçã", "Banana", "Manga"]

for i in frutas:
 print(i)



for letra in "Python":
 print(letra) '''

########################

#While

#O while é um loop com condição, como no exemplo abaixo, o código vai se repetir até que a variavel contenha o valor 5

'''contador = 0 
while contador < 5 :  
  print(contador)
  contador += 1''' ##Output : 0 1 2 3 4

########################

##Break

'''for i in range(10):
  if i == 5:
    break #O break interrompe o loop
  print(i)''' ##Output : 0 1 2 3 4 

########################

##Continue

'''for i in range(10):
  if i == 5:
    continue #o comando "continue" pula o restante e vai para a proxima repetição
  print(i)   ## Output : 0 1 2 3 4 6 7 8 9'''

########################

## else nos loops

#O else nos loops roda o código após o loop ser encerrado de forma natural (sem o break)

'''for i in range(5):
  print(i)
else:
  print("O loop terminou!")'''


########################

##Loops Aninhados

#Loops aninhados são loops dentro de loops, sendo que o loop externo comanda o interno e o interno determina
#quantas vezes o externo vai se repetir, para cada "loop concluido" interno, o loop externo passa para a proxima "fase"

'''for i in range(3):
  for j in range(2):
    print(i, j)'''

'''for hora in range(3):
  for minuto in range(60):
    print(hora, ":", minuto)'''

########################    

##enumerate
#O enumerate serve para literalmente enumerarmos uma sequencia de valores, sem a necessidade de fazer de uma forma a mais bruta (com o i += 1)
'''frutas = ["Maçã", "Banana", "Abacaxi"]

for indice, fruta in enumerate(frutas):
  print(indice, fruta)'''


########################

##zip - percorrer listas juntas

'''nomes = ["Ana", "João", "Lioner"]
idades = [20, 25, 18]

for nome, idade in zip(nomes, idades):
  print(nome, idade)'''

'''nomes = ["Lioner", "Ana", "Jorge"]
idades = [18, 20, 30]

for i, (nome, idade) in enumerate(zip(nomes, idades)): #também é possivel juntar enumerate com zip.
  print(i, nome, idade)'''