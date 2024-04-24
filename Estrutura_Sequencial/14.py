# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele 
# traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de 
# R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso aquantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

quantidade_peixe = float(input("\nInforme a quantidade de peixe em Kg: "))
excesso = quantidade_peixe - 50
multa = 4 * excesso

if (quantidade_peixe <= 50):
    print (f"\nNão existe peso excedente. Você pescou {quantidade_peixe}Kg, e é permitido pescar até 50 Kg.")
else:
    print(f"\nVocê pescou {quantidade_peixe} Kg de peixe. O máximo permitido é 50 Kg, existe um excedente de {excesso} Kg.")
    print ("O valor da multa a ser paga devido ao excesso de peso é: R$", multa)