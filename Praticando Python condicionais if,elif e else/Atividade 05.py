#05) Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.
despesa_mensal = float(input("Insira a despesa mensal: "))
if(despesa_mensal < 0): #Se a despesa mensal for menor que 0, emitirá valor inválido,não executando o restante do código
  print("Valor inválido!")
else:
  if(despesa_mensal > 3000):
    print("Atenção! Você ultrapassou o limite de orçamento.")
  else:
    print("Está tudo nos conformes!")
