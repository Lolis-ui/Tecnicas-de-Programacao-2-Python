nome1 = input("Digite seu nome: ")
peso1 = float(input(f"Digite o seu peso, {nome1}: "))

nome2 = (input("Digite o seu nome: "))
peso2 = float(input(f"Digite o seu peso, {nome2}: "))

if peso1 > peso2: 
    print(f"{nome1} tem {peso1} kilos, tendo um peso maior que {nome2}")
elif peso1 == peso2:
    print(f"As duas pessoas {nome1} e o {nome2} tem o mesmo peso")
else: 
    print(f"A {nome2} tem {peso2} kilos, tendo um peso maior que {nome1}")