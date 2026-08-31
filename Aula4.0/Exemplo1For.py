#For para percorrer uma lista e verificar a quantidade de caracteres

nomes = ["Felipe", "Maria", "Luiza", "Paulo", "Josefina"]

for i in nomes:
    #len conta a quantidade de caracteres
    if len(i) != 4:
        continue
    print(f"Esse nome tem quatro letras: {i}")
    
    if i == "Paulo":
        break
    print("Terminou a execução, tchau")