#17) Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias
#Observações:
  #1 litro --> 6m
  #1 lata de de 18 litros custa 80,00
  #1 galão de 3,6 custa 25,00

#Biblioteca necessária para fazer o arredondamento.
import math

area_metros = float(input("Informe a área a ser pintada: "))

#Se a área for menor igual a 0, será dado como área inválida, não executando o restante do código.
if(area_metros <= 0):
  print("Área inválida!")
else:
  #Cálculo para saber a quantidade de tinta necessária.
  litros = (area_metros / 6)

  #Folga de 10% que será dada à quantidade de litros necessária.
  folga = litros * 0.10
  litros = litros + folga
  litros = math.ceil(litros)

  #Situação A: Apenas latas de 18 litros.

  #Calcula a quantidade de latas necessárias.
  latas_necessarias = (litros / 18)
  latas_necessarias = math.ceil(latas_necessarias)

  #Cálcula o preço total das latas necessárias.
  preco_latas = latas_necessarias * 80

  #Situação B: Apenas galões de 3,6 litros.

  #Calcula a quantidade de galões necessários.
  galoes_necessarios = (litros / 3.6)
  galoes_necessarios = math.ceil(galoes_necessarios)

  #Calcula o preço total dos galões necessários.
  preco_galoes = galoes_necessarios * 25

  #Situação C: Misturar latas e galões.

  #Calculo da quantidade de latas necessárias.
  mistura_latas = (litros / 18)
  mistura_latas = math.floor(mistura_latas)

  #Cálculo da quantidade restante de tinta que será preenchida com os galões.
  litros_necessarios = mistura_latas * 18
  tinta_restante = litros - litros_necessarios

  #Cálculo da quantidade de galões necessárias.
  mistura_galoes = (tinta_restante / 3.6)
  mistura_galoes = math.ceil(mistura_galoes)

  #Calcula o preço total da mistura de latas e galões.
  preco_mistura_latas = (mistura_latas * 80)
  preco_mistura_galoes = (mistura_galoes * 25)
  preco_total = (preco_mistura_latas + preco_mistura_galoes)


  print("Situação A:")
  print(f"Quantidade de latas necessárias: {latas_necessarias}")
  print(f"Preço total das latas: R${preco_latas}\n")

  print("Situação B:")
  print(f"Quantidade de galões necessários: {galoes_necessarios}")
  print(f"Preço de galões necessários: R${preco_galoes}\n")

  print("Situação C:")
  print(f"Quantidade da mistura de latas: {mistura_latas}")
  print(f"Quantidade da mistura de galões: {mistura_galoes}")
  print(f"Preço de latas e galões necessários: R${preco_total}\n")

  #Essa estrutura de decisão irá decidir qual a opção mais econômica baseado nos preços de cada situação.
  if(preco_latas < preco_galoes and preco_latas < preco_total):
    print("A opção A é a mais econômica.")
  elif(preco_galoes < preco_latas and preco_galoes < preco_total):
    print("A opção B é a mais econômica.")
  elif(preco_total < preco_latas and preco_total < preco_galoes):
    print("A opção C é a mais econômica.")
  elif(preco_latas == preco_galoes and preco_latas == preco_total and preco_galoes == preco_total):
    print("Qualquer opção será a mais econômica.")
  elif(area_metros <= 54): #De 54 metros para baixo a situação b quanto c se igualam.
    print("Tanto a situação B quanto C será econômica.")
