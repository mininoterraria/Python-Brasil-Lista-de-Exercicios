#15) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

ganho_por_hora = float(input("Insira o ganho por hora: "))
horas_trabalhadas_mes = float(input("Insira as horas trabalhadas no mês: "))

#Caso ganho por hora ou horas trabalhadas no mes seja menor ou igual a 0, dará como inválido, não executando o cálculo do código.
if(ganho_por_hora <= 0 or horas_trabalhadas_mes <= 0):
  print("Um ou mais valores não pode ser menor igual a 0.")
else:
  #Cálculo do salário bruto
  salario_bruto = ganho_por_hora * horas_trabalhadas_mes

  #Cálculo do imposto de renda
  imposto_renda = salario_bruto * 0.11

  #Cálculo do inss
  inss = salario_bruto * 0.08

  #Cálculo do sindicato
  sindicato = salario_bruto * 0.05

  #Total de descontos
  descontos = (imposto_renda + inss + sindicato)

  #Salário liquido gerado pelos descontos.
  salario_liquido = salario_bruto - descontos


  print(f"+ Salário Bruto: R$ {salario_bruto}")
  print(f"- IR (11%): R$ {imposto_renda}")
  print(f"- INSS (8%): R$ {inss}")
  print(f"- Sindicato(5%): R$ {sindicato}")
  print(f"= Salário Liquido: R$ {salario_liquido}")
