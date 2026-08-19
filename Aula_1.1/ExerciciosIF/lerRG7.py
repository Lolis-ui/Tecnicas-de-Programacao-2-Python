while True:
    rg = input("\nRG do empregado: ")
    ano_nasc = int(input("Ano de nascimento: "))
    ano_ingresso = int(input("Ano de ingresso na empresa: "))
    ano_atual = int(input("Ano atual: "))

    idade = ano_atual - ano_nasc
    tempo = ano_atual - ano_ingresso

    print(f"\nRG: {rg}")
    print(f"Idade: {idade} anos")
    print(f"Tempo de trabalho: {tempo} anos")
    
    if idade >= 65 or tempo >= 30 or (idade >= 60 and tempo >= 25):
        print("\nREQUERER APOSENTADORIA")

        if idade >= 65:
            print("→ Por idade (65+ anos)")
        if tempo >= 30:
            print("→ Por tempo de serviço (30+ anos)")
        if idade >= 60 and tempo >= 25:
            print("→ Por idade e tempo (60+ e 25+ anos)")
    else:
        print("\nNÃO REQUERER APOSENTADORIA")
    
    # Continua?
    resp = input("\nOutro empregado? (S/N): ").upper()
    if resp == 'N':
        print("\nFIM DO PROGRAMA")
        break