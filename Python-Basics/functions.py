'''
def eh_par(x):
  return x %2 == 0
  
print(eh_par(3))

#############
def dobro(a):
  return a*2

valor = dobro(float(input("Escolha um número para ser duplicado : ")))

print(valor)'''

def analisar_numeros(lista):
  total = 0
  pares = []
  impares = []
  for n in lista:
    total += n
    if n % 2 == 0 :
      pares.append(n)
    else:
      impares.append(n)
  if lista == []:
      media = 0
  else:  
      media = total / (len(lista))
  final = {
  "pares" : pares,
  "impares" : impares,
  "total" : total,
  "media" : media
  }
  return final

print(analisar_numeros([]))



def aoquadrado(lista):
  return [n**2 for n in lista]


lista = [2, 4]
resultado = aoquadrado(lista)

print(lista)
print(resultado)


## FINALMENTE !!!!! AGORA VOU IR PRO NUMPY! ORGULHO!