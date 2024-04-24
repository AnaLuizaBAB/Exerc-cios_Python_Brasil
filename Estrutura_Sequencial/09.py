# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. 
# C = 5 * ((F-32) / 9).

fahrenheit = float(input("\nInforme a temperatura em Fahrenheit que gostaria de transformar em Celsius: "))

celsius = 5 * ((fahrenheit - 32)/9)

print (f"\n{fahrenheit} Fahrenheit é igual a {celsius: .2f} graus Celsius")