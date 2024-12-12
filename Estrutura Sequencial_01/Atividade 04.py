#04) Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota_1 = float(input("Insira a primeira nota: "))
nota_2 = float(input("Insira a segunda nota: "))
nota_3 = float(input("Insira a terceira nota: "))
nota_4 = float(input("Insira a quarta nota: "))

#Se qualquer uma das notas for menor que 0, dará como valor inválido, não executando o restante do código.
if(nota_1 or nota_2 or nota_3 or nota_4 < 0):
  print("Um ou mais notas inválidas!")
else:
  media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
  print(f"Média bimestral: {media}")
