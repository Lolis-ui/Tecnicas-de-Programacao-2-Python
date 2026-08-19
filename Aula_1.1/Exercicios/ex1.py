import os
os.system("cls")
salario = 1500
bonus = 150

QTD = int(input("Digite a quantidade de itens vendidos: "))
salarioTotal = salario + (bonus * QTD)

print(f"O salário Total desse mês é de: {salarioTotal}")