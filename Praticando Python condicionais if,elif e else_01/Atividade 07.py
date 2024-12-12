#07) Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, ficaram de recuperação ou reprovados. As regras são:

#Média >= 7: Aprovado
#5 <= Média < 7: Recuperação
#Média < 5: Reprovado
#Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno.
nota_1 = float(input("Insira a nota 1: "))
nota_2 = float(input("Insira a nota 2: "))
nota_3 = float(input("Insira a nota 3: "))
if(nota_1 < 0 or nota_1 > 10 or nota_2 < 0 or nota_2 > 10 or nota_3 < 0 or nota_3 > 10): #Caso uma das notas seja menor que 0 ou maior que 10, emitirá como valor inválido, não executando o restante do código
  print("Um ou mais valores inválidos!")
else:
  media = ((nota_1 + nota_2 + nota_3)/ 3)
  print(f"{media}")
  if(media >= 7):
    print("Aprovado!")
  elif(media < 7 and media >= 5):
    print("Recuperação!")
  else:
    print("Reprovado!")
