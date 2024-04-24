# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário 
# no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que 
# nos dê:
# a. salário bruto.
# b. quanto pagou ao INSS.      
# c. quanto pagou ao sindicato.     
# d. o salário líquido.
# Obs.: Salário Bruto - Descontos = Salário Líquido

salario_hora = float (input("\nInforme o valor recebido por hora: "))
quantidade_horas = float (input("Informe a quantidades de horas que foram trabalhadas no mês: "))

salario_bruto = salario_hora * quantidade_horas
imposto = 0.11 * salario_bruto
inss = 0.08 * salario_bruto
sindicato = 0.05 * salario_bruto
salario_liquido = salario_bruto - (imposto + inss + sindicato)

print (f"\nSalário bruto: R$ {salario_bruto:.2f}")
print (f"Valor a ser descontado devido ao inss: R$ {inss:.2f}")
print (f"Valor a ser descontado devido ao sindicato: R$ {sindicato:.2f} ")
print (f"Salário líquido: R$ {salario_liquido:.2f} ")