#Lê os valores e armazena em uma lista(vetor)
#Comando Append paraadicionar os dados do vetor

lista = []

for i in range(1,6):
    num = int(input(f"Digite o {i}° número"))
    lista.append(num)
    
print("Números armazenados na lista")
for i in lista:
    print(i)