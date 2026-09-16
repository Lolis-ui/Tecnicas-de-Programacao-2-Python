class Pessoa: 
    def __init__(self,nome,idade):
     self.nome = nome
     self.idade = idade
        
    def calcularIdade(self):
            ano = int(input("Digite o ano atual: "))
            return ano- self.idade
        
p1 = Pessoa('Luiz', 25)
print(p1.calcularIdade()) 