op = input("Digite uma letra do alfabeto: ")

match op.upper():
    case "A"|"E"|"I"|"O"|"U"|"Y":
        print("Você Digitou uma Vogal")
    case "B"|"C"|"D"|"F"|"G"|"H"|"J"|"K"|"L"|"M"|"N"|"P"|"Q"|"R"|"S"|"T"|"V"|"W"|"X"|"Z":
        print("Você digitou uma consoante")
    case _:
        print("Opção Inválida")