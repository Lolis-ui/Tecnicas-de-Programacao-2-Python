num = int(input("Digite um número: "))

if(num %2 == 0 and num > 0):
    quadrado = num**2
    print("O número selecionado é par!")
    print(f"O valor do quadrado do número {num} é de: {quadrado}")
elif(num %2 != 0): 
    print("O número informado não é par!")
else: 
    print("O número informado não é positivo")
