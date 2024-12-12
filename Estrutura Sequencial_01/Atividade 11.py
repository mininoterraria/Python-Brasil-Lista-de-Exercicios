#11) Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a.o produto do dobro do primeiro com metade do segundo
#b.a soma do triplo do primeiro com o terceiro.
#c.o terceiro elevado ao cubo.

numero_inteiro1 = int(input("Insira um número inteiro: "))
numero_inteiro2 = int(input("Insira outro número inteiro: "))
numero_real = float(input("Insira um número flutuante: "))

#Situação A: Faz a multiplicação de valor1 * 2 e valor2 / 2.
situacao_a = (numero_inteiro1 * 2) * (numero_inteiro2 / 2)

#Situação B: Faz a adição de valor1 * 3 e valor3.
situacao_b = (numero_inteiro1 * 3) + (numero_real)

#Situação C: Faz a exponenciação do valor3.
situacao_c = numero_real ** 3

print(f"Situação A: {situacao_a}")
print(f"Situação B: {situacao_b}")
print(f"Situação C: {situacao_c}")
