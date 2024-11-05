#02) Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.
#Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.
at_1 = int(input("Insira os dias para atividade 1: "))
at_2 = int(input("Insira os dias para atividade 2: "))
at_3 = int(input("Insira os dias para atividade 3: "))
if(at_1 < 0 or at_2 < 0 or at_3 < 0): #Caso uma das atividades seja menor que 0, emitirá um erro.
  print("Erro: Os dias não podem ser negativos!")
else:
  print(f"Quantidade de dias totais: {at_1 + at_2 + at_3}")
