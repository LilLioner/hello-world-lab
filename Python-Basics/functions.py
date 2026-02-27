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
  media = total / (len(lista))
  return pares, impares, total, media

print(analisar_numeros([1,2,3,4]))