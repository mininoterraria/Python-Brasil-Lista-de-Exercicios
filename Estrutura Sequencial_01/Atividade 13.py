#13) Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura = float(input("Insira a altura: "))

#Se altura for menor ou igual a 0 retornará inválido, não executando o código do cálculo.
if(altura <= 0):
  print("Altura Inválida!")
else:
  #Cálculo de peso ideal masculino.
  peso_ideal_masculino = (72.7 * altura) - 58

  #Cálculo de peso ideal feminino.
  peso_ideal_feminino = (62.1 * altura) - 44.7

  print(f"Peso ideal masculino: {peso_ideal_masculino:.2f}kg")
  print(f"Peso ideal feminino: {peso_ideal_feminino:.2f}kg")
