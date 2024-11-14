#12) Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Insira a altura: "))

if(altura <= 0):
  #Caso altura seja menor ou igual a 0 retornará altura inválida!
  print("Altura Inválida!")
else:
  #Fórmula do cálculo do peso ideal.
  peso_ideal = (72.7 * altura) - 58

  print(f"Peso ideal: {peso_ideal:.2f}kg")
