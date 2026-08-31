import os
os.system("cls")

nota1 = float(input("Digite nota1"))
nota2 = float(input("Digite nota2"))
media = (nota1 + nota2)/2

if media > 7.0: 
    print(f"Aluno Aprovado, a média é: {media}")
elif media > 4 and media < 6.9:
    print(f"Aluno está de exame, a média é: {media}")
else: 
    print(f"Aluno Reprovado :( {media}")
