class Funcionario:
    def __init__(self):
        self.__nomeFunc = ""
        self.__idade = 0
        self.__salarioAtual = 0
        self.__aumentoSal = 0

    @property
    def _nomeFunc(self):
        return self.__nomeFunc

    @_nomeFunc.setter
    def _nomeFunc(self, value):
        self.__nomeFunc = value

    @property
    def _idade(self):
        return self.__idade

    @_idade.setter
    def _idade(self, value):
        self.__idade = value

    @property
    def _salarioAtual(self):
        return self.__salarioAtual

    @_salarioAtual.setter
    def _salarioAtual(self, value):
        self.__salarioAtual = value

    @property
    def _aumentoSal(self):
        return self.__aumentoSal

    @_aumentoSal.setter
    def _aumentoSal(self, value):
        self.__aumentoSal = value
        
    def cadastrarFuncionario(self):
        self.__nomeFunc = input("Digite o nome do funcionário: ")
        self.__idade = int(input("Digite a idade: "))
        self.__salarioAtual = float(input("Digite o salário atual: "))
    
    def calculaAumenta10(self):
        self.__aumentoSal = self.__salarioAtual + (self.__salarioAtual *10)/100
        print(f"O salário com o aumento de 10% R$ {self.__aumentoSal}")
        
    def calculaAumenta15(self):
        self.__aumentoSal = self.__salarioAtual + (self.__salarioAtual *15)/100
        print(f"O salário com o aumento de 15% R$ {self.__aumentoSal}")
    
    def mostrarFuncionario(self):
        print(f"Nome do funcionário: {self.__nomeFunc}\n Idade: {self.__idade} \n Salário Atual: {self.__salarioAtual}")
        
    
        
        

    