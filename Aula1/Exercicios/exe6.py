#Reajuste de salario 
salario = float(input("Digite o valor do seu salário: "))
porcentagem = int(input("Digite a pocentagem de aumento do seu salário: "))

novoSalario = (salario * porcentagem)/100 + salario
print(f"O valor do seu novo salario com o aumento de {porcentagem}% é de: {novoSalario}")
