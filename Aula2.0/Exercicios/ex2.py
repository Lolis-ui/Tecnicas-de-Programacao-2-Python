import os
os.system("cls")
valorParcela = float(input("Digite o valor da parcela: "))
taxa = int(input("Digite a taxa de juros: "))
mesesAtraso = int(input("Alguma parcela em atraso? Digite a quantidade: "))

valorAtraso = valorParcela + (valorParcela * (taxa/100) * mesesAtraso)
print(f"O valor total a ser pago pelo móvel será de: {valorAtraso}")
print(f"Valor da taxa de juros: {taxa}")
print(f"Valor da parcela: {valorParcela}")