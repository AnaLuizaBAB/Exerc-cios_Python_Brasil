# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a coberturada tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidadesde latas de tinta a serem compradas e o preço total.

import math

area_pintada = float (input("\nInforme a área a ser pintada em metros quadrados: "))
quantidade_tinta = area_pintada / 3         # informa a quantidade de litros necessários
quantidade_latas = quantidade_tinta / 18    # informa a quantidade de latas necessárias
gasto = (math.ceil(quantidade_latas)) * 80  

print (f"\nSerão pintados {area_pintada} m²")
print (f"Para isso serão necessárias {math.ceil(quantidade_latas)} latas.") 
print (f"E o valor do investimento será de: R$ {gasto:.2f}")