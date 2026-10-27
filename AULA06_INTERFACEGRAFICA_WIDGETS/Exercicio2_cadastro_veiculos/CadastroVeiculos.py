from tkinter import *
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import sys
import sqlite3


class CadastroVeiculos:

    def __init__(self):
        self.tela = Tk()
        self.configurar_tela()
        self.criar_banco()
        self.criar_componentes()

    def configurar_tela(self):
        self.tela.title("Cadastro de Veículos")
        self.tela.config(background="#1844bf")

        self.largura = 900
        self.altura = 700

        self.var = StringVar(value="utilitario")

        largura_screen = self.tela.winfo_screenwidth()
        altura_screen = self.tela.winfo_screenheight()

        posx = largura_screen / 2 - self.largura / 2
        posy = altura_screen / 2 - self.altura / 2

        self.tela.geometry("%dx%d+%d+%d" % (self.largura, self.altura, posx, posy))

    def criar_banco(self):
        self.conn = sqlite3.connect("veiculos.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS veiculos(
            codigo INTEGER PRIMARY KEY AUTOINCREMENT,
            nomeVeiculo TEXT,
            placa TEXT,
            modelo TEXT,
            marca TEXT,
            utilitario TEXT
        )
        """)
        self.conn.commit()

    def salvar(self):
        try:
            self.cursor.execute("""
                INSERT INTO veiculos (nomeVeiculo, placa, modelo, marca, utilitario)
                VALUES (?, ?, ?, ?, ?)
            """, (
                self.txt_nomeVeiculo.get(),
                self.txt_placa.get(),
                self.txt_modelo.get(),
                self.cmb_marca.get(),
                self.var.get()
            ))
            self.conn.commit()
            print("Veículo cadastrado com sucesso!")
            self.Consultar()
            self.limpar_campos()
        except Exception as e:
            print(f"Erro ao cadastrar veículo: {e}")

    def Consultar(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        self.cursor.execute(
            "SELECT codigo, nomeVeiculo, placa, modelo, marca, utilitario FROM veiculos"
        )
        for row in self.cursor.fetchall():
            self.tree.insert("", "end", values=row)

    def atualizar(self):
        selecao = self.tree.selection()
        if not selecao:
            print("Selecione um veículo para atualizar.")
            return

        codigo = self.tree.item(selecao[0], "values")[0]

        self.cursor.execute("""
            UPDATE veiculos SET
                nomeVeiculo = ?,
                placa = ?,
                modelo = ?,
                marca = ?,
                utilitario = ?
            WHERE codigo = ?
        """, (
            self.txt_nomeVeiculo.get(),
            self.txt_placa.get(),
            self.txt_modelo.get(),
            self.cmb_marca.get(),
            self.var.get(),
            codigo
        ))
        self.conn.commit()
        self.Consultar()
        self.limpar_campos()

    def excluir(self):
        selecao = self.tree.selection()
        if not selecao:
            print("Selecione um veículo para excluir.")
            return

        codigo = self.tree.item(selecao[1], "values")[0]
        self.cursor.execute("DELETE FROM veiculos WHERE codigo=?", (codigo,))
        self.conn.commit()
        self.Consultar()
        self.limpar_campos()

    def limpar_campos(self):
        self.txt_nomeVeiculo.delete(0, END)
        self.txt_placa.delete(0, END)
        self.txt_modelo.delete(0, END)
        self.cmb_marca.current(0)
        self.var.set("utilitario")

    def escolher_imagem(self):
        caminho = filedialog.askopenfilename(
            title="Escolha uma imagem",
            filetypes=[("Arquivos de imagem", "*.png;*.jpg;*.jpeg")]
        )
        if not caminho:
            return

        imagem = Image.open(caminho)
        largura, altura = imagem.size
        nova_largura = 110
        nova_altura = int(altura * (nova_largura / largura))
        imagem = imagem.resize((nova_largura, nova_altura))

        imagem_tk = ImageTk.PhotoImage(imagem)
        self.lbl_imagem = Label(self.tela, image=imagem_tk, bg="gray")
        self.lbl_imagem.image = imagem_tk
        self.lbl_imagem.place(x=750, y=50)

    def sair(self):
        self.conn.close()
        self.tela.destroy()
        sys.exit()

    def selecionar_item(self, event):
        selecao = self.tree.selection()
        if not selecao:
            return

        dados = self.tree.item(selecao[0], "values")

        self.txt_nomeVeiculo.delete(0, END)
        self.txt_nomeVeiculo.insert(0, dados[1])

        self.txt_placa.delete(0, END)
        self.txt_placa.insert(0, dados[2])

        self.txt_modelo.delete(0, END)
        self.txt_modelo.insert(0, dados[3])

        self.cmb_marca.set(dados[4])
        self.var.set(dados[5])

    def criar_componentes(self):
        Label(self.tela, text="Cadastro de Veículos",
              font=("Arial", 16, "bold"), bg="#1844bf", fg="white").place(x=10, y=10)

        Label(self.tela, text="Nome do Veículo:", bg="#1844bf", fg="white").place(x=10, y=50)
        Label(self.tela, text="Placa:",           bg="#1844bf", fg="white").place(x=10, y=90)
        Label(self.tela, text="Modelo:",          bg="#1844bf", fg="white").place(x=10, y=130)
        Label(self.tela, text="Marca:",           bg="#1844bf", fg="white").place(x=10, y=170)
        Label(self.tela, text="Utilitário:",      bg="#1844bf", fg="white").place(x=10, y=210)

        self.txt_nomeVeiculo = Entry(self.tela, width=30)
        self.txt_nomeVeiculo.place(x=150, y=50)

        self.txt_placa = Entry(self.tela, width=30)
        self.txt_placa.place(x=150, y=90)

        self.txt_modelo = Entry(self.tela, width=30)
        self.txt_modelo.place(x=150, y=130)

        self.cmb_marca = ttk.Combobox(
            self.tela,
            values=["Toyota", "Honda", "Ford", "Chevrolet", "Volkswagen",
                    "Fiat", "Renault", "Hyundai", "Nissan", "Jeep"],
            width=27,
            state="readonly"
        )
        self.cmb_marca.place(x=150, y=170)
        self.cmb_marca.current(0)

        Radiobutton(self.tela, text="Utilitário", variable=self.var,
                    value="utilitario", bg="#1844bf", fg="white").place(x=150, y=210)
        Radiobutton(self.tela, text="Não utilitário", variable=self.var,
                    value="nao_utilitario", bg="#1844bf", fg="white").place(x=250, y=210)

        Button(self.tela, text="Escolher Imagem",
               command=self.escolher_imagem).place(x=10, y=260)

        try:
            self.foto_salvar    = PhotoImage(file="icones/salvar.png")
            self.foto_excluir   = PhotoImage(file="icones/excluir.png")
            self.foto_alterar   = PhotoImage(file="icones/alterar.png")
            self.foto_consultar = PhotoImage(file="icones/consultar.png")
            self.foto_sair      = PhotoImage(file="icones/sair.png")
        except Exception as e:
            print("Ícones não encontrados, usando botões sem imagem:", e)
            self.foto_salvar = self.foto_excluir = self.foto_alterar = \
                self.foto_consultar = self.foto_sair = None

        Button(self.tela, text="Salvar",    image=self.foto_salvar,
               compound=TOP, command=self.salvar).place(x=10, y=320)
        Button(self.tela, text="Consultar", image=self.foto_consultar,
               compound=TOP, command=self.Consultar).place(x=110, y=320)
        Button(self.tela, text="Atualizar", image=self.foto_alterar,
               compound=TOP, command=self.atualizar).place(x=210, y=320)
        Button(self.tela, text="Excluir",   image=self.foto_excluir,
               compound=TOP, command=self.excluir).place(x=310, y=320)
        Button(self.tela, text="Sair",      image=self.foto_sair,
               compound=TOP, command=self.sair).place(x=410, y=320)

        self.tree = ttk.Treeview(
            self.tela,
            columns=("codigo", "nomeVeiculo", "placa", "modelo", "marca", "utilitario"),
            show="headings"
        )
        self.tree.heading("codigo",      text="Código")
        self.tree.heading("nomeVeiculo", text="Nome do Veículo")
        self.tree.heading("placa",       text="Placa")
        self.tree.heading("modelo",      text="Modelo")
        self.tree.heading("marca",       text="Marca")
        self.tree.heading("utilitario",  text="Utilitário")

        self.tree.column("codigo", width=60)
        self.tree.place(x=10, y=420, width=870, height=250)

        self.tree.bind("<ButtonRelease-1>", self.selecionar_item)

    def executar(self):
        self.tela.mainloop()