# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit

celsius = float(input("\nInforme a temperatura em graus Celsius que pretende transformar em Fahrenheit: "))

fahrenheit = (celsius * 1.8) + 32

print (f"\n{celsius}° Celsius corresponde a {fahrenheit: .2f}° Fahrenheit.")

print("\n")