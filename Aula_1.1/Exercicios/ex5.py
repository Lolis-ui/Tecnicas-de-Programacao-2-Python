custoFabricacao = float(input("Digite o custo de fabricação da Pick-Up: "))

distribuidora = (38/100) * custoFabricacao 
impostos = (47/100) * custoFabricacao
valorTotal = custoFabricacao + distribuidora + impostos

print(f"O custo de fabricação é de: {custoFabricacao}")
print(f"Imposto da distribuidora: {distribuidora}")
print(f"Outros impostos: {impostos}")
print(f"Valor Total da Pick-Up: {valorTotal}")


