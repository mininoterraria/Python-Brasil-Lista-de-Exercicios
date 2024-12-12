#01) Faça um Programa que peça dois números e imprima o maior deles.

numero_01 = int(input("Insira o primeiro número: "))
numero_02 = int(input("Insira o segundo número: "))

#Estrutura de decisão para ver qual número é maior.
if(numero_01 > numero_02):
  print("Número 1 é maior que Número 2.")
  print(numero_01)
elif(numero_02 > numero_01):
  print("Número 2 é maior que Número 1.")
  print(numero_02)
else:
  print("Os números são iguais.")
