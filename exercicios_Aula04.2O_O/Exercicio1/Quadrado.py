class Quadrado:
    def __init__(self):
        self.__numero = 0
        self.__resultado = 0

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, value):
        self.__numero = value
        self.__resultado = value ** 2

    @property
    def resultado(self):
        return self.__resultado

    def calcularQuadrado(self):
        self.numero = int(input("Digite o número desejado: "))

    def mostrarQuadrado(self):
        print(f"O resultado do número {self.numero}² é de: {self.resultado}")

        
    