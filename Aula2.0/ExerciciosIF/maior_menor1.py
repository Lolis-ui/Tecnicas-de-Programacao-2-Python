num1 = int(input("Digite o valor do primero número: "))
num2 = int(input("Digite o valor do segundo número: "))

if num1 > num2: 
    divisao = num1/num2
    print(f"A divisão do maior número {num1} pelo menor {num2} é de: {divisao}")
elif num1 < num2: 
    divisao = num2/num1
    print(f"A divisão do maior número {num2} pelo menor {num1} é de: {divisao}")
else: 
    print("Os números são iguais")