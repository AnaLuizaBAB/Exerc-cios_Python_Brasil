# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# a.Para homens: (72.7*h) - 58
# b.Para mulheres: (62.1*h) - 44.7

print ("\nInforme o seu gênero.")
genero = input ("Digite M para masculino ou F para feminino: ").upper().strip()
altura = float (input("Informe a sua altura em metros: "))

peso_M = (72.7 * altura) - 58
peso_F = (62.1 * altura) - 44.7

if (genero == "F"):
    print(f"\nSeu peso ideal de acordo com a altura informada ({altura}m) é: {peso_F: .2f}Kg")
else:
    print(f"\nSeu peso ideal de acordo com a altura informada ({altura}m) é: {peso_M: .2f}Kg")