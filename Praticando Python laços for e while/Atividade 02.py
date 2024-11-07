#02) Você está desenvolvendo um programa que calcula a soma de todos os números de uma lista. Seu objetivo é garantir que o programa percorra corretamente a lista e acumule o valor total de todos os números presentes.
numeros = [10, 20, 30, 40, 50]
soma = 0
for numero in numeros:
  soma += numero
print(f"Soma total dos valores: {soma}")
