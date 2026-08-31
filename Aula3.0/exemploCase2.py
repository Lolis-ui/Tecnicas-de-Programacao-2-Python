op = int(input("Digite um número de um a seis"))

match op: 
    case 1|2|3:
        print("Você digitou 1 2 ou 3")
    case 4|5|6:
        print("Você digitou 4 5 ou 6")
    case _:
        print("Opção incorreta")
