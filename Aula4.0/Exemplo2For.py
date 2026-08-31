localiza = input("Digite uma fruta: ")

frutas = ["Banana", "Maça", "Abacate", "Manga", "Pera", "Kiwi"]
for i in frutas: 
    if i == localiza:
        print(f"{localiza}, Fruta encontrada")
        break
    else: 
        print(f"{localiza}, Não encontrada até o momento")