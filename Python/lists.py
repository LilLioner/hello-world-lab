lista = [1, 2, 3, 4]

emptylst = list()
emptylst2 = []

lista_aninhada = [1, 2, 3, 4,["Hello", "World!"], 5, 6]

## lista por compreensão de lista

numeros = [1, 2, 3, 4]

numerosdouble = [n * 2 for n in numeros]

print(numerosdouble)

## Acessar elementos na lista

#para acessar um elemento em especifico, basta inserir a var escolhida + o numero do indice do valor desejado (começando do 0)

acesso = ["Hello", "Lioner", "World!", "Brazil!"]
print(acesso[0], acesso[2]) 

print(acesso[0], acesso[-1]) #no caso de utilizarmos numeros negativos, a linguagem passará a usar os ultimos valores da lista

#print(acesso[5]) #Caso voce selecione numeros de indice fora do alcance da lista, o resultado será um Index Error, list out of range

## Adicionar, remover e alterar valores das lists

addict = [1, 2 , 3]
addict.append(4)

print(addict)

print(addict[1])

addict[1] = 0  # Para alterarmos um valor, basta selecionar o numero de indice desejado do valor e alteralo normalmente.
print(addict[1])

del addict[1] #o comando para deletar um valor é bem simples e autoexmplicativo após vermos os comandos anteriores
print(addict)
print(addict[1]) # A partir do momento que um valor é deletado, os numeros seguintes tem o numero de indice diminuido em 1

##Verificando se a lista está vazia

vazia = []

if len(vazia) == 0: #O comando "len" serve para identificar quantos valores possuem uma lista
  print("A lista está vazia")
else:
  print("A lista contém valores")

contain = ["Valor"]

if vazia: #essa é uma forma mais simples de verificar se uma lista contém ou nao valores
  print("A lista está vazia")
else:
  print("A lista contém valores")

  ## Buscando elementos na lista  
# essa função serve para conferrir se um valor especifico está presente na lista
element = ["Valor", "Hello", "World!"]

print("Valor" in element) #True
print("Lioner" in element) #False
print("World!" in element) #True

## Juntando listas 

jun = [1, 2, 3]
to = [4, 5, 6]

junto = to+jun #output : 4 5 6 1 2 3

print(junto)