'''um programa que leia nome e media de um aluno, mostrando no final a situação do aluno, tundo isso em um dicionarrio'''

pessoa = {
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
  print(f"O {k} é igual a {v}")