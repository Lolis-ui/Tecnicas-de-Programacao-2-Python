aluno = input("Digite o nome do aluno : ")
nota1 = float(input("Digite a primera nota: "))
nota2 = float(input("Digite a segunda nota: "))
idade = int(input("Digite a idade do aluno"))

media = (nota1 + nota2)/2

print(f"O aluno {aluno}, teve a média = {media:.2f}")
print("O aluno" + aluno + "teve a média: " + str(media))