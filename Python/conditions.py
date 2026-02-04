## Aprovado ou reprovado a partir de nota de 4 bimestres.

print("Vamos calcular a o resultado final de aluno com base na média dos bimestres:")
fst = float(input("Digite a nota tirada no primeiro Bimestre: "))
scd = float(input("Digite a nota tirada no segundo Bimestre: "))
thd = float(input("Digite a nota tirada no terceiro Bimestre: "))
fth = float(input("Digite a nota tirada no quarto Bimestre: "))

if (fst+scd+thd+fth)/4 >= 6 :
  print("Aluno aprovado com nota: ", (fst+scd+thd+fth)/4)
else :
  print("Aluno reprovado com a nota: ", (fst+scd+thd+fth)/4)