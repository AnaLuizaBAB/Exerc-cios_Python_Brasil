# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário 
# no referido mês.

valor_da_hora = float(input ("\nInforme o valor de sua hora trabalhada: "))
horas_trabalhadas = float(input("Informe a quantidade de horas trabalhadas no mês: "))

pagamento = valor_da_hora * horas_trabalhadas

print(f"\nO valor a ser recebido é igual a: {pagamento: .2f}")