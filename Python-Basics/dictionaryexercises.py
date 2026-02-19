'''um programa que leia nome e media de um aluno, mostrando no final a situação do aluno, tundo isso em um dicionarrio'''

'''pessoa = {
  "Nome":"",
  "Média":"",
  "situação":""
}

pessoa["Nome"] = str(input("Qual o nome do aluno? \n"))
pessoa["Média"] = float(input("Qual a média do aluno? \n"))

if pessoa["Média"] >= 6:
  pessoa["situação"] = "Aprovado"
else:
  pessoa["situação"] = "Reprovado"
  
for k, v in pessoa.items():
  print(f"O {k} é igual a {v}")'''

produto = {
  "nome" : "Mouse",
  "preco" : 120,
  "estoque": 20
}

print(produto["preco"])
print(produto["estoque"])
print(produto.keys())

produto["preco"] = 180
produto["estoque"] -= 3

print(produto)  

#########################


'''carro = {
    "marca": "Ford",
    "modelo": "Fiesta"
}

carro["ano"] = 2000 ##O ano é so um exemplo
carro["cor"] = "Vermelho"
print(carro)'''

pessoa = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "São Paulo"
}

'''for k in pessoa:
  print(f'Chave: {k}')

for v in pessoa.values():
  print(f'Valore: {v}')

for k, v in pessoa.items():
  print(f'{k} é igual a : {v}')'''

palavra = str(input("Digite uma palavra : "))
letras = {}

for l in palavra.lower():
  if l.isspace():
    continue
  letras[l] = letras.get(l, 0) + 1
  
print(letras)

vendas = {
    "jan": 1500,
    "fev": 2300,
    "mar": 1800
}

total = 0

for v in vendas.values():
  total += v

print(f"valor total:{total}, média de vendas:{total/len(vendas)}")