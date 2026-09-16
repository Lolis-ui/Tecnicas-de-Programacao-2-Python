#define nome da classe
class Produto: 
    #define o xonstrutor da classeinicializando os atributos
    def __init__(self):
        #atributis private dois undeline __ define o atributo como privado
        self.__nome = ""
        self.__valor = 0
        self.__quantidade = 0
    #Encapsulamento dos atributos
    #Pressione ctrl + shift + p => digite Getter and Setter
    @property
    def _nome(self):
        return self.__nome

    @_nome.setter
    def _nome(self, value):
        self.__nome = value

    @property
    def _valor(self):
        return self.__valor

    @_valor.setter
    def _valor(self, value):
        self.__valor = value

    @property
    def _quantidade(self):
        return self.__quantidade

    @_quantidade.setter
    def _quantidade(self, value):
        self.__quantidade = value
        
    #Método cadastrar produto
    def cadastrarProduto(self):
        print("\n Cadastro de Produtos")
        self.__nome = input("Digite o nome do Produto: ")
        self.__quantidade = int(input("Digite a quantidade: "))
        self.__valor = float(input("Digite o valor do produto: "))
        print("Produto cadastrado com sucesso !!!")
        
        #Método mostrar produto
    def mostrarProduto(self):
            print("\n Dados do Produto")
            print("Nome do produto: ", self.__nome)
            print("Quantidade: ", self.__quantidade)
            print("Valor: ", self.__valor)
            
        #Método com retorno calcular total
    def calcular_valor_total(self):
            return self.__valor * self.__quantidade

    
        