#09) Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

temperatura_fahrenheit = float(input("Insira a temperatura em fahrenheit: "))

#Fórmula de conversão de fahrenheit para celsius.
conversao_celsius = 5 * ((temperatura_fahrenheit - 32) / 9)

print(f"A conversão de fahrenheit para celsius é: {conversao_celsius}°C")
