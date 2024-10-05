import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def atualizar_lista(nome):
    ...

#interface grafica com tkinter
janelaPrincipal = tk.Tk()
janelaPrincipal.title("CRUD de Funcionarios")

#Campo de pesquisa
tk.Label(janelaPrincipal, text="Pesquisar por Nome: ").grid(row=0, column=0, padx=10, pady=10)

entry_pesquisa = tk.Entry(janelaPrincipal)
entry_pesquisa.grid(row=0, column=1, padx=10, pady=10)
entry_pesquisa.bind("<KeyRelease>", lambda event: atualizar_lista(entry_pesquisa.get()))

#Botões
btn_adicionar = tk.Button(janelaPrincipal, text="Adicionar", command='')
btn_adicionar.grid(row=0, column=2, padx=10, pady=10)

btn_alterar = tk.Button(janelaPrincipal, text="Alterar", command='')
btn_alterar.grid(row=0, column=3, padx=10, pady=10)

btn_deletar = tk.Button(janelaPrincipal, text="Deletar", command='')
btn_deletar.grid(row=0, column=4, padx=10, pady=10)

#Grid (Treeview) para exibir a lista de funcionários
tree = ttk.Treeview(janelaPrincipal, columns=("ID", "Nome", "Idade", "Cargo", "Departamento", "Salario", "Telefone", "Email"))
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Idade", text="Idade")
tree.heading("Cargo", text="Cargo")
tree.heading("Departamento", text="Departamento")
tree.heading("Salario", text="Salario")
tree.heading("Telefone", text="Telefone")
tree.heading("Email", text="Email")

janelaPrincipal.mainloop()