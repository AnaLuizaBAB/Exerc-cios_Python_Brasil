# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input("\nInforme a medida do lado do quadrado: "))

area = lado * lado
dobro_da_area = 2 * area

print (f"\nA área do quadrado é {area: .2f}")
print (f"O valor correspondente ao dobro da area do quadrado é: {dobro_da_area: .2f}")