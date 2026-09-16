from Quadrado import Quadrado

class Principal:
    @staticmethod
    def main():
        quad = Quadrado()

        while True:
                op = int(input(
                    "\nDigite a opção:"
                    "\n 1 - Calcular Quadrado"
                    "\n 2 - Mostrar Dados"
                    "\n 0 - Sair do Sistema"
                    "\n> "
                ))
                match op:
                    case 0:
                        print("Saindo do Sistema...")
                        break
                    case 1:
                        quad.calcularQuadrado()
                    case 2:
                        quad.mostrarQuadrado()
                    case _:
                        print("Digite um número válido")


if __name__ == "__main__":
    Principal.main()