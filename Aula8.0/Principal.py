from Clientes import CadastroClientes

class Principal:
    @staticmethod
    def main(): 
        #Instanciar o objeto da classe CadastroClientes
        cli = CadastroClientes()
        cli.executar()  # Chamar o método executar para iniciar a interface gráfica

if __name__ == "__main__":
    Principal.main()  # Chamar o método main da classe Principal
        