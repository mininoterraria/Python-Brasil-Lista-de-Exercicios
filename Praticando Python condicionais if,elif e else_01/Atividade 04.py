#04) Anna Júlia está criando um sistema para calcular o Índice de Massa Corporal (IMC) e fornecer recomendações básicas. O programa deve receber o peso e a altura de uma pessoa e exibir o valor do IMC, além de indicar se está abaixo do peso, com peso normal ou acima do peso. Crie um programa que receba o peso (em kg) e a altura (em metros) e calcule o IMC usando a fórmula: IMC = peso / (altura ** 2) Depois, exiba o valor do IMC e uma mensagem indicando se está abaixo do peso (IMC < 18.5), peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).
peso = float(input("Insira o peso em kg: "))
altura = float(input("Insira a altura em metros: "))
if(peso <= 0 or altura <= 0): #Caso peso ou altura seja menor igual a 0, emitirá valor inválido, não executando o restante do código
  print("Um ou mais valores inválidos!")
else:
  imc = peso / (altura ** 2)
  print(f"{imc:.2f}")
  if(imc < 18.5):
    print("Está abaixo do peso!")
  elif(imc >= 18.5 and imc <= 25):
    print("Peso Normal!")
  else:
    print("Está acima do peso!")
