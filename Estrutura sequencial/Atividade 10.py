#10) Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
#F = (°C x 1.8) + 32

temperatura_celsius = float(input("Insira a temperatura em celsius: "))

#Fórmula de conversão de celsius para fahrenheit.
conversao_fahrenheit = (temperatura_celsius * 1.8) + 32

print(f"A conversão de celsius para fahrenheit é: {conversao_fahrenheit}°F")
