nascimento = int(input("Digite o ano do seu nascimento: "))
nome = input("Digite seu nome: ")
anoAtual = int(input("Digite o ano atual: "))

idade = anoAtual - nascimento
print(f"{nome}, nascida(o) no ano de {nascimento} tem {idade} anos de idade")