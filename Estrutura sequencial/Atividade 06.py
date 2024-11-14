#06) Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input("Insira o raio do circulo: "))

#Se o raio for menor igual a 0 retorna um erro, não executando o restante do código.
if(raio <= 0):
  print("Raio inválido!")
else:
  
  #Faz o cálculo da área do círculo.
  area_circulo = 3.1415926535898 * (raio ** 2) #** -> Calcula a potência.

  print(f"A área do circulo é: {area_circulo}")
