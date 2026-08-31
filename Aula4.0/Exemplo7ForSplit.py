#Só devemos digitar os valores com espaço

num = input("Digite os númers deixando espaços entre eles: ")
vetor = [int(i) for i in num.split()]
print("Valores armazenados: ", vetor)