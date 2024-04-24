# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a. o produto do dobro do primeiro com metade do segundo .
# b. a soma do triplo do primeiro com o terceiro.
# c. o terceiro elevado ao cubo

a = float (input("\nInforme um número inteiro: "))
b = float (input("Informe outro número inteiro: "))
c = float (input("Informe um número real, diferente dos informados anteriormente: "))

x = (2 * a) * (b / 2)
y = (3 * a) + c
z = c**3

print (f"\nO primeiro, segundo e terceiro números informados foram respectivamente: {a}, {b}, {c}")
print("\nO produto do dobro do primeiro com metade do segundo é: ", x)
print("A soma do triplo do primeiro com o terceiro é: ", y)
print ("O terceiro elevado ao cubo é: ", z)