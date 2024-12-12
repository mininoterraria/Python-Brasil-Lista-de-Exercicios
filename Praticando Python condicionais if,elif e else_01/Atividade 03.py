#03) Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.
temperatura_atual = float(input("Insira a temperatura atual: "))
if(temperatura_atual > 25):
  print("Alerta! Temperatura acima do limite permitido!")
else:
  print("Tudo nos conformes!")
