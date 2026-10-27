from CadastroVeiculos import CadastroVeiculos


class Principal:
    @staticmethod
    def main():
        cad = CadastroVeiculos()
        cad.executar()


if __name__ == "__main__":
    Principal.main()