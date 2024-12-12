#16) Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

#Biblioteca necessária para fazer o cálculo de arredondamento.
import math

area_metros = float(input("Insira o tamanho da área a ser pintada em metros quadrados: "))

#Se a area for menor ou igual a 0, dará como inválida, não executando o restante do código.
if(area_metros <= 0):
  print("Área inválida!")
else:
  #Calcula a quantidade de litros necessários.
  litros = (area_metros / 3)

  #Calcula a quantidade de latas necessárias.
  latas_necessarias = (litros / 18)
  latas_necessarias = math.ceil(latas_necessarias)

  #Calcula o preço das latas
  preço_latas = latas_necessarias * 80

  #Define se a frase ficará no singular ou plural de acordo com a quantidade de latas.
  if(latas_necessarias == 1):
    frase = "Será necessário 1 lata."
  else:
    frase = f"Serão necessárias {latas_necessarias} latas"

  print(frase)
  print(f"Preço total: R$ {preço_latas}")
