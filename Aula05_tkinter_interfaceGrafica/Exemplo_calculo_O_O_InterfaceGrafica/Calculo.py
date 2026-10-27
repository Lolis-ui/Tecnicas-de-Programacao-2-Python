from tkinter import *

class Calculadora:
    def __init__(self):
        self.__num1 = 0.0
        self.__num2 = 0.0
        self.__resultado = 0.0

    # ----- Properties -----
    @property
    def num1(self):
        return self.__num1

    @num1.setter
    def num1(self, value):
        self.__num1 = value

    @property
    def num2(self):
        return self.__num2

    @num2.setter
    def num2(self, value):
        self.__num2 = value

    @property
    def resultado(self):
        return self.__resultado

    @resultado.setter
    def resultado(self, value):
        self.__resultado = value

    # ----- Configuração da tela -----
    def configurarTela(self):
        self.tela = Tk()
        self.tela.title("Calculadora")
        self.tela.configure(background="lightblue")
        self.tela.geometry("700x500")
        self.tela.resizable(True, True)

    # ----- Layout dos widgets -----
    def criar_layout(self):
        # Título
        self.lblTitulo = Label(self.tela, text="Calculadora",
                               font=("Arial", 16), bg="lightblue", fg="black")
        self.lblTitulo.place(x=300, y=20)

        # Número 1 - Label
        self.lblNum1 = Label(self.tela, text="Número 1:",
                             font=("Arial", 12), bg="lightblue", fg="black")
        self.lblNum1.place(x=50, y=100)

        # Número 1 - Entry
        self.txtNum1 = Entry(self.tela, font=("Arial", 12), width=30)
        self.txtNum1.place(x=150, y=100)

        # Número 2 - Label
        self.lblNum2 = Label(self.tela, text="Número 2:",
                             font=("Arial", 12), bg="lightblue", fg="black")
        self.lblNum2.place(x=50, y=150)

        # Número 2 - Entry
        self.txtNum2 = Entry(self.tela, font=("Arial", 12), width=30)
        self.txtNum2.place(x=150, y=150)

        # Botão Calcular
        self.btnCalcular = Button(self.tela, text="Calcular", command=self.calcular,
                                  font=("Arial", 12), bg="green", fg="white")
        self.btnCalcular.place(x=150, y=200)

        # Label Resultado (criado uma vez só)
        self.lblResultado = Label(self.tela, text="Resultado:",
                                  font=("Arial", 12), bg="lightblue", fg="black")
        self.lblResultado.place(x=150, y=250)

    # ----- Ação do botão -----
    def calcular(self):
        try:
            self.num1 = float(self.txtNum1.get())
            self.num2 = float(self.txtNum2.get())
            self.resultado = self.num1 + self.num2

            self.lblResultado.config(text=f"Resultado: {self.resultado}")
        except ValueError:
            self.lblResultado.config(text="Resultado: Erro! Digite números válidos.")

    # ----- Executar aplicação -----
    def executar(self):
        self.configurarTela()
        self.criar_layout()
        self.tela.mainloop()


# Programa principal
if __name__ == "__main__":
    app = Calculadora()
    app.executar()