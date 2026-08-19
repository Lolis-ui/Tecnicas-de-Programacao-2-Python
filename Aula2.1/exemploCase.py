op = int(input("1-sacar \n 2- Extrato \n3-Sair"))

match op: 
    case 1: 
        print("Você escolheu sacar")
    case 2: 
        print("Você escolheu extrato")
    case 1: 
        exit
    case _:
        print("Opcao inválida")
        