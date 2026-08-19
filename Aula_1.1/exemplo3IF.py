negativado = int(input("Possui nome negativo? 1-Sim 0-Não" ))
if negativado != 1 or negativado != 0:
    print("Digite apenas 1 ou 0")
if negativado == 1:
    print("Não pode realizar empréstimo")
else:
    cart_assinada = int(input("Possui carteira assinada? 1-Sim 0-Não" ))
    if cart_assinada == 0:
        print("Não pode realizar empréstimo")
    else:
        print("Pode realizar empréstimo")