#08) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_hora = float(input("Informe seu ganho por hora: "))
horas_trabalhadas_mes = float(input("Informe as horas trabalhadas por mês: "))

#Se o ganho por hora ou horas trabalhadas por mês for menor que 0 será dado como inválido, não executando o código do cálculo.
if(ganho_hora or horas_trabalhadas_mes < 0):
  print("Um ou mais valores inválidos!")
else:
  #Faz o cálculo do salário multiplicando ganho por hora por horas trabalhadas no mês.
  salario = ganho_hora * horas_trabalhadas_mes
  
  print(f"Salário mensal: R${salario}")
