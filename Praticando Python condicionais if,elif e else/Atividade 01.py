#01) Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.
#Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.
maca = int(input("Insira a quantidade de maçãs vendidas: "))
banana = int(input("Insira a quantidade de bananas vendidas: "))
if(maca < 0 or banana < 0): #Caso uma das frutas seja menor que 0, exibirá valor inválido, não executando o restante do código
  print("Um ou mais valores inválidos!")
else:
  if(maca > banana):
    print("As maçãs venderam mais!")
  elif(maca < banana):
    print("As bananas venderam mais!")
  else:
    print("Ambas tiveram a mesma quantidade de vendas!")
