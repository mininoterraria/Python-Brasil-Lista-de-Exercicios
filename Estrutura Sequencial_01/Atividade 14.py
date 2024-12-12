#14) João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso_peixe = float(input("Insira a quantidade em quilos do peixe: "))

#Caso o peso do peixe seja menor ou igual a 0, dará como inválido, não executando o cálculo do código.
if(peso_peixe <= 0):
  print("Valor de peso inválido!")
else:
  #O cálculo de excesso e multa só será feito caso o peso do peixe ultrapasse 50kg.
  if(peso_peixe > 50):
    excesso = peso_peixe - 50
    multa = excesso * 4
    print(f"O peixe contém {excesso}kg excedente, pagará uma multa de R$ {multa}")
  else:
    #Essa print será feita caso não haja multa por quilo excedente.
    print(f"O peixe contém {peso_peixe}kg, não haverá multa!")
