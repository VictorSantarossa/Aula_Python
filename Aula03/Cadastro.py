import tkinter as tk
from tkinter import messagebox

def click():
    messagebox.showinfo("Cadastro",f"Cadastrado Realizado Com Sucesso, {entryNome.get()}")

janela = tk.Tk()
janela.geometry("800x600")
janela.title("Cadastro Cliente")

labelNome = tk.Label(janela,text = "Digite seu nome:", font=("Arial", 16, "bold"), fg="gray", bg="black")
labelNome.pack(ipadx = 10, pady = (20,2))
entryNome = tk.Entry(janela)
entryNome.pack(ipadx= 100, pady= 5)

labelEndereco = tk.Label(janela,text = "Digite seu Endereço:", font=("Arial", 16, "bold"), fg="gray", bg="black")
labelEndereco.pack(ipadx = 10, pady = (40,2))
entryEndereco = tk.Entry(janela)
entryEndereco.pack(ipadx= 100, pady= 5)

labelTelefone = tk.Label(janela,text = "Digite seu Telefone:", font=("Arial", 16, "bold"), fg="gray", bg="black")
labelTelefone.pack(ipadx = 10, pady = (40,2))
entryTelefone = tk.Entry(janela)
entryTelefone.pack(ipadx= 100, pady= 5)

button_First = tk.Button(janela, text="Gravar", command = click, font=("Arial", 16, "bold"), fg="black")
button_First.pack(ipadx= 50, pady= 20)

janela.mainloop()
