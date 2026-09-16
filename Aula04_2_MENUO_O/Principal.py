from Funcionario import Funcionario

class Principal: 
    @staticmethod
    def main():
        func = Funcionario()
    
        while True:  
            op = int(input("Digite a opção: \n 1-Cadastrar Funcionario \n 2-Mostrar Dados \n 3-Aumento de 10% \n 4-Aumento de 15% \n 0-Sair do Sistema \n"))   
            match(op):
                case 0: 
                    print("Saindo do Sistema...")
                    break
                case 1: 
                    func.cadastrarFuncionario()
                case 2: 
                    func.mostrarFuncionario()
                case 3: 
                    func.calculaAumenta10()
                case 4: 
                    func.calculaAumenta15()
                case _:
                    print("Digite um número válido")

if __name__ == "__main__":
    Principal.main()