#06) Mariana é responsável por liberar o acesso ao escritório e precisa de um programa que verifique se os funcionários podem entrar. Para isso, ela usará o horário atual. O escritório só permite acesso entre 8h e 18h. Crie um programa que receba a hora atual como entrada (em formato de 24 horas) e exiba uma mensagem informando se o acesso é permitido ou negado.
hora_atual = int(input("Insira o horário atual: "))
if(hora_atual < 0 or hora_atual > 24): #Se a hora atual for menor que 0 ou maior que 24, emitirá um horário inválido, não executando o restante do código
  print("Horário inválido!")
else:
  if(hora_atual >= 8 and hora_atual <= 18):
    print("Acesso liberado!")
  else:
    print("Acesso negado!")
