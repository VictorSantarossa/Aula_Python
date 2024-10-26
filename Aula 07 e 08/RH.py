import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


# Conexão com o banco de dados SQLite
conexao = sqlite3.connect('funcionarios.db')
cursor = conexao.cursor()

# Cria a tabela se ela não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS funcionarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    idade INTEGER,
                    cargo TEXT,
                    departamento TEXT,
                    salario REAL,
                    telefone TEXT,
                    email TEXT)''')
conexao.commit()


def atualizar_lista(nome):
    ...

# Campos de entrada 
def adicionar_funcionario():

    def Cancelar():
        janelaAdicionar.destroy()

    def Gravar():
        try:
            cursor.execute('INSERT INTO funcionarios (nome, idade, cargo, departamento, salario, telefone, email) VALUES (?, ?, ?, ?, ?, ?, ?)',
                       (entryNome.get(),
                        entryIdade.get(),
                        entryCargo.get(),
                        entryDepartamento.get(),
                        entrySalario.get(),
                        entryTelefone.get(),
                        entryEmail.get()))
        
            conexao.commit()
            messagebox.showinfo("Sucesso", "Funcionário adicionado com sucesso!")
            janelaAdicionar.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
        
    janelaAdicionar = tk.Toplevel(janelaPrincipal)
    janelaAdicionar.title('Adicionar Funcionário')

    labelNome = tk.Label(janelaAdicionar, text="Nome: ")
    labelNome.grid(row=0, column=0, padx=5, pady=5, sticky='w')
    entryNome = tk.Entry(janelaAdicionar, width=50)
    entryNome.grid(row=0, column=1, padx=10, pady=5, sticky='w')

    labelIdade = tk.Label(janelaAdicionar, text="Idade: ")
    labelIdade.grid(row=1, column=0, padx=5, pady=5, sticky='w')
    entryIdade = tk.Entry(janelaAdicionar, width=50)
    entryIdade.grid(row=1, column=1, padx=10, pady=5, sticky='w')

    labelCargo = tk.Label(janelaAdicionar, text="Cargo: ")
    labelCargo.grid(row=2, column=0, padx=5, pady=5, sticky='w')
    entryCargo = tk.Entry(janelaAdicionar, width=50)
    entryCargo.grid(row=2, column=1, padx=10, pady=5, sticky='w')

    labelDepartamento = tk.Label(janelaAdicionar, text="Departamento: ")
    labelDepartamento.grid(row=3, column=0, padx=5, pady=5, sticky='w')
    entryDepartamento = tk.Entry(janelaAdicionar, width=50)
    entryDepartamento.grid(row=3, column=1, padx=10, pady=5, sticky='w')

    labelSalario = tk.Label(janelaAdicionar, text="Salário: ")
    labelSalario.grid(row=4, column=0, padx=5, pady=5, sticky='w')
    entrySalario = tk.Entry(janelaAdicionar, width=50)
    entrySalario.grid(row=4, column=1, padx=10, pady=5, sticky='w')

    labelTelefone = tk.Label(janelaAdicionar, text="Telefone: ")
    labelTelefone.grid(row=5, column=0, padx=5, pady=5, sticky='w')
    entryTelefone = tk.Entry(janelaAdicionar, width=50)
    entryTelefone.grid(row=5, column=1, padx=10, pady=5, sticky='w')

    labelEmail = tk.Label(janelaAdicionar, text="Email: ")
    labelEmail.grid(row=6, column=0, padx=5, pady=5, sticky='w')
    entryEmail = tk.Entry(janelaAdicionar, width=50)
    entryEmail.grid(row=6, column=1, padx=10, pady=5, sticky='w')

    buttonGravar = tk.Button(janelaAdicionar, text="Gravar", command=Gravar)
    buttonGravar.grid(row=7, column=0, columnspan=2, padx=(10, 50), pady=5)

    buttonCancelar = tk.Button(janelaAdicionar, text="Cancelar", command=Cancelar)
    buttonCancelar.grid(row=7, column=1, columnspan=2, padx=(50, 10), pady=5)


# Interface gráfica com Tkinter
janelaPrincipal = tk.Tk()
janelaPrincipal.title("CRUD de Funcionários")

# Campo de pesquisa
tk.Label(janelaPrincipal, text="Pesquisar por Nome:").grid(row=0, column=0, padx=10, pady=10)

entry_pesquisa = tk.Entry(janelaPrincipal)
entry_pesquisa.grid(row=0, column=1, padx=10, pady=10)
entry_pesquisa.bind("<KeyRelease>", lambda event: atualizar_lista(entry_pesquisa.get()))

# Botões
btn_adicionar = tk.Button(janelaPrincipal, text="Adicionar", command=adicionar_funcionario)
btn_adicionar.grid(row=0, column=2, padx=10, pady=10)

btn_alterar = tk.Button(janelaPrincipal, text="Alterar", command='')
btn_alterar.grid(row=0, column=3, padx=10, pady=10)

btn_deletar = tk.Button(janelaPrincipal, text="Deletar", command='')
btn_deletar.grid(row=0, column=4, padx=10, pady=10)

# Grid (Treeview) para exibir a lista de funcionários
tree = ttk.Treeview(janelaPrincipal, columns=("ID", "Nome", "Idade", "Cargo", "Departamento", "Salário", "Telefone", "Email"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nome", text="Funcionário")
tree.heading("Idade", text="Idade")
tree.heading("Cargo", text="Cargo")
tree.heading("Departamento", text="Departamento")
tree.heading("Salário", text="Salário")
tree.heading("Telefone", text="Telefone")
tree.heading("Email", text="Email")
tree.grid(row=1, column=0, columnspan=5, padx=10, pady=10)


janelaPrincipal.mainloop()
