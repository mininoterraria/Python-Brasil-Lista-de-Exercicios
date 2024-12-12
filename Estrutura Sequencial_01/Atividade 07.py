#07) Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input("Insira o lado do quadrado: "))

#Se o lado for menor igual a 0 retorna um erro, não executando o restante do código.
if(lado <= 0):
  print("Lado inválido!")
else:
  #Cálcula a área do quadrado
  area_quadrado = lado ** 2 #** -> Calcula a potência.

  print(f"O dobro da área do quadrado é: {area_quadrado * 2}")
