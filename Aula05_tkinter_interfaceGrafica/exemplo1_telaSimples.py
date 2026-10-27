from tkinter import *

# Criação da janela principal
tela = Tk()
tela.title("Tela Simples")
tela.configure(background="lightblue")
tela.geometry("700x500")

# Para não permitir que o usuário redimensione a tela
# tela.resizable(False, False)

# Tamanho mínimo da tela
tela.minsize(width=700, height=500)

# Tamanho máximo da tela
tela.maxsize(width=1000, height=800)

# Campo Nome
lbl_nome = Label(tela, text="Nome:", font=("Arial", 12), bg="blue", fg="white")
lbl_nome.place(x=50, y=50)

txt_nome = Entry(tela, font=("Arial", 12), width=30)
txt_nome.place(x=150, y=50)

# Campo Endereço
lbl_endereco = Label(tela, text="Endereço:", font=("Arial", 12), bg="blue", fg="white")
lbl_endereco.place(x=50, y=100)

txt_end = Entry(tela, font=("Arial", 12), width=30)
txt_end.place(x=150, y=100)

# Função para mostrar a mensagem
def mostrarmsg():
    lbl_mensagem = Label(tela, text=f"Nome: {txt_nome.get()} | Endereço: {txt_end.get()}", font=("Arial", 12), bg="lightblue", fg="black")
    lbl_mensagem.place(x=150, y=200)

btn_botao = Button(tela, text="Enviar", command=mostrarmsg, font=("Arial", 12), bg="green", fg="white")
btn_botao.place(x=150, y=150)

# Comando para executar a tela
tela.mainloop()