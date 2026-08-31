opcao = 1

while opcao != 0:
    print("\nMenu")
    print("1- Pagar à vista")
    print("2- Cartão de Débito")
    print("3- Cartão de Crédito")
    print("0- Sair")
    print("ESCOLHA UMA OPÇÃO")

    opcao = int(input("Digite uma opção: "))

    if opcao == 0:
        print("Programa encerrado!")
        break
    
    if opcao in [1, 2, 3]:
        precoTotal = float(input("Digite o valor da compra: R$ "))
        
        match opcao:
            case 1:
                desconto = precoTotal * 0.15  # 15% de desconto
                totalDesconto = precoTotal - desconto
                print(f"Valor da compra: R$ {precoTotal:.2f}")
                print(f"Desconto: R$ {desconto:.2f}")
                print(f"Valor com desconto: R$ {totalDesconto:.2f}")
                
            case 2:
                desconto = precoTotal * 0.10  # 10% de desconto
                totalDesconto = precoTotal - desconto
                print(f"Valor da compra: R$ {precoTotal:.2f}")
                print(f"Desconto: R$ {desconto:.2f}")
                print(f"Valor com desconto: R$ {totalDesconto:.2f}")
                
            case 3:
                desconto = precoTotal * 0.05  # 5% de desconto
                totalDesconto = precoTotal - desconto
                print(f"Valor da compra: R$ {precoTotal:.2f}")
                print(f"Desconto: R$ {desconto:.2f}")
                print(f"Valor com desconto: R$ {totalDesconto:.2f}")
    else:
        print("Opção inválida! Escolha uma das opções (0, 1, 2 ou 3)")