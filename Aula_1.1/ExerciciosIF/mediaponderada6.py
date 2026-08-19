opcao = -1
while opcao !=0: 
    num1 = int(input("Digite um número positivo: "))
    if(num1 < 0): 
        print("NÚMERO INVÁLIDO! O NÚMERO DIGITADO NÃO É POSITIVO")
        break
    num2 = int(input("Digite um outro número positivo: "))
    if(num2 < 0): 
        print("NÚMERO INVÁLIDO! O NÚMERO DIGITADO NÃO É POSITIVO")
        break
    else: 
        print("MENU")
        print("1- Calcular Média ponderada(com pesos 2 e 3 respectivamente): ")
        print("2- Calcular Quadrado dos números: ")
        print("3- Calcular o cubo do menor número: ")
        print("ESCOLHA UMA OPÇÃO")

        opcao = int(input("Digite sua opcao: "))
        if(opcao ==1):
            mediaponderada = (num1 *2 + num2*3)/5
            print(f"A media ponderada é de: {mediaponderada}")
        elif(opcao ==2):
            quadrado1 = num1 **2
            quadrado2 = num2 **2
            print(f"Quadrado do número {num1}: {quadrado1}")
            print(f"Quadrado do número {num2}: {quadrado2}")
        elif(opcao ==3):
            if(num1 < num2):
                cubo1 = num1 **3
                print(f"O cubo do menor número é de: {cubo1}")
            else:
                        cubo2 = num2 **3
                        print(f"O cubo do menor número é de: {cubo2}")
        else: 
            print("Opção inválida!! Escolha um número do Menu")
            

        
    