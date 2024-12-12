#10) Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:

#O valor da renda mensal precisa ser maior que R$ 2.000,00.
#O valor da parcela não pode ultrapassar 30% da renda.
#Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima.
renda_mensal = float(input("Insira a renda mensal: "))
parcela_desejada = float(input("Insira a parcela desejada: "))
if(renda_mensal < 0 or parcela_desejada < 0): #Se a renda mensal for menor que 0 ou parcela desejada for menor que 0, emitirá valor inválido, não executando o restante do código.
  print("Um ou mais valores inválidos!")
else:
  parcela_maxima = renda_mensal * 0.3
  print(f"Parcela máxima permitida de acordo com a renda atual: R${parcela_maxima}")
  if(renda_mensal < 2000):
    print("Empréstimo negado: renda mensal insuficiente!")
  elif(parcela_desejada > parcela_maxima):
    print("Empréstimo negado: Parcela acima dos 30% da renda!")
  else:
    print("Empréstimo liberado!")
