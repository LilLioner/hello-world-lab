a = {} # Dict vazia, mesmo conceito da lista vazia

b = dict() #Dict vazia... também na mesma lógica.

c = {"a": 1, "b": 2}
d = dict(nome="Lioner", idade=19) # Chaves viram strings (Obs: a:b   a->chave, b->valor)

print(d["nome"])

# Dicionarios e listas são estruturas de dados semelhantes, a diferença é que com os dicionarios, não temos a obrigação de usar indices numericos 

dados = {
  "nome" : "Lioner",
  "idade" : 19,
  "CPF" : 12345678900
}

print("Nome =", dados["nome"], "Idade = ", dados["idade"], "CPF =", dados["CPF"])
dados["sexo"] = "M"

print(dados["sexo"])

del dados["idade"]
#print(dados["idade"]) SyntaxError

jogo = {
  'nome': "God of War",
  'ano': "2018",
  'Produtor(a)': "Santa Monica"
}

print(jogo.values())
print(jogo.keys())
print(jogo.items())

for k, v in jogo.items():
  print("O", k, "é", v)

for k, v in jogo.items():
  print(f'O {k} é {v}')