opcao = 1

while opcao!=0:
    print("Calculo de Grandezas Elétricas (0 para parar)")
    print("1- Tensão em Volt: ")
    print("2- Resistência em Ohm")
    print("3- Corrente em Ampére")
    print("ESCOLHA UMA OPÇÃO")

    opcao = int(input("Digite uma opção: "))
    match opcao: 
        case 1: 
            R = float(input("Digite o valor da resistência elétrica em Ohm: "))
            I = float(input("Digite o valor da corrente em Amperes: "))
            tensao = R*I
            print(f"Tensão Elétrica: {tensao}")
        case 2: 
            U = float(input("Digite o valor da tensão elétrica em Volts: "))
            I = float(input("Digite o valor da corrente em Amperes: "))
            resistencia = U/I
            print(f"Resistência em Ohm: {resistencia}")
        case 3:
            U = float(input("Digite a tensão em Volts"))
            R = float(input("Digite o valor da resistência elétrica em Ohm: "))
            corrente = U/R
            print(f"Corrente em Amperes: {corrente}")
        case 0: 
            print("Programa encerrado")
        case _:
            print("Opção inválida! Escolha uma das opções")
        