import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Conexão com o banco de dados SQLite
conexao = sqlite3.connect('Tarefas.db')
cursor = conexao.cursor()

# Cria a tabela se ela não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS Tarefas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    descricao TEXT,
                    tempo INTEGER,
                    status TEXT,
                    responsavel TEXT,
                    importante TEXT)''')  # Adicionado campo "importante"
conexao.commit()

# Função para buscar Tarefas no banco de dados
def buscar_tarefa(nome=""):
    cursor.execute("SELECT * FROM Tarefas WHERE nome LIKE ?", ('%' + nome + '%',))
    return cursor.fetchall()

# Função para atualizar o grid com a lista de Tarefas
def atualizar_lista(nome=""):
    for row in tree.get_children():
        tree.delete(row)
    tarefas = buscar_tarefa(nome)
    for tarefa in tarefas:
        tree.insert("", "end", values=tarefa)

# Função para adicionar uma Tarefa ao banco de dados
def adicionar_tarefa():
    def salvar_tarefa():
        nome = entry_nome.get()
        descricao = entry_descricao.get()
        tempo = entry_tempo.get()
        status = "Completo" if var_status_completo.get() else "Incompleto"
        importante = "Sim" if var_status_importante.get() else "Não"
        responsavel = entry_responsavel.get()

        if nome and descricao and tempo and responsavel and importante:
            cursor.execute("INSERT INTO Tarefas (nome, descricao, tempo, status, responsavel, importante) VALUES (?, ?, ?, ?, ?, ?)", 
                           (nome, descricao, tempo, status, responsavel, importante))
            conexao.commit()
            atualizar_lista()
            janela_add.destroy()
        else:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")

    janela_add = tk.Toplevel(root)
    janela_add.title("Adicionar Tarefa")
    
    # Campos de entrada
    tk.Label(janela_add, text="Nome").grid(row=0, column=0)
    entry_nome = tk.Entry(janela_add)
    entry_nome.grid(row=0, column=1)

    tk.Label(janela_add, text="Descrição").grid(row=1, column=0)
    entry_descricao = tk.Entry(janela_add)
    entry_descricao.grid(row=1, column=1)

    tk.Label(janela_add, text="Tempo").grid(row=2, column=0)
    entry_tempo = tk.Entry(janela_add)
    entry_tempo.grid(row=2, column=1)

    tk.Label(janela_add, text="Status").grid(row=3, column=0)
    var_status_completo = tk.BooleanVar()
    check_status = tk.Checkbutton(janela_add, text="Completo", variable=var_status_completo)
    check_status.grid(row=3, column=1)

    tk.Label(janela_add, text="Importante").grid(row=4, column=0)
    var_status_importante = tk.BooleanVar()
    check_importante = tk.Checkbutton(janela_add, text="Importante", variable=var_status_importante)
    check_importante.grid(row=4, column=1)

    tk.Label(janela_add, text="Responsável").grid(row=5, column=0)
    entry_responsavel = tk.Entry(janela_add)
    entry_responsavel.grid(row=5, column=1)

    # Botão para salvar a tarefa
    btn_salvar = tk.Button(janela_add, text="Salvar", command=salvar_tarefa)
    btn_salvar.grid(row=6, columnspan=2)

# Função para deletar uma Tarefa do banco de dados
def deletar_tarefa():
    item_selecionado = tree.selection()
    if item_selecionado:
        tarefa = tree.item(item_selecionado)['values']
        cursor.execute("DELETE FROM Tarefas WHERE id=?", (tarefa[0],))
        conexao.commit()
        atualizar_lista()
    else:
        messagebox.showerror("Erro", "Selecione uma tarefa para deletar.")

# Função para alterar uma tarefa
def alterar_tarefa():
    item_selecionado = tree.selection()
    if item_selecionado:
        tarefa = tree.item(item_selecionado)['values']

        def salvar_alteracao():
            nome = entry_nome.get()
            descricao = entry_descricao.get()
            tempo = entry_tempo.get()
            status = "Completo" if var_status_completo.get() else "Incompleto"
            importante = "Sim" if var_status_importante.get() else "Não"
            responsavel = entry_responsavel.get()

            cursor.execute("UPDATE Tarefas SET nome=?, descricao=?, tempo=?, status=?, responsavel=?, importante=? WHERE id=?", 
                           (nome, descricao, tempo, status, responsavel, importante, tarefa[0]))
            conexao.commit()
            atualizar_lista()
            janela_editar.destroy()

        janela_editar = tk.Toplevel(root)
        janela_editar.title("Alterar Tarefa")

        # Campos de entrada
        tk.Label(janela_editar, text="Nome").grid(row=0, column=0)
        entry_nome = tk.Entry(janela_editar)
        entry_nome.insert(0, tarefa[1])
        entry_nome.grid(row=0, column=1)

        tk.Label(janela_editar, text="Descrição").grid(row=1, column=0)
        entry_descricao = tk.Entry(janela_editar)
        entry_descricao.insert(0, tarefa[2])
        entry_descricao.grid(row=1, column=1)

        tk.Label(janela_editar, text="Tempo").grid(row=2, column=0)
        entry_tempo = tk.Entry(janela_editar)
        entry_tempo.insert(0, tarefa[3])
        entry_tempo.grid(row=2, column=1)

        tk.Label(janela_editar, text="Status").grid(row=3, column=0)
        var_status_completo = tk.BooleanVar(value=tarefa[4] == "Completo")
        check_status = tk.Checkbutton(janela_editar, text="Completo", variable=var_status_completo)
        check_status.grid(row=3, column=1)

        tk.Label(janela_editar, text="Importante").grid(row=4, column=0)
        var_status_importante = tk.BooleanVar(value=tarefa[6] == "Sim")
        check_importante = tk.Checkbutton(janela_editar, text="Importante", variable=var_status_importante)
        check_importante.grid(row=4, column=1)

        tk.Label(janela_editar, text="Responsável").grid(row=5, column=0)
        entry_responsavel = tk.Entry(janela_editar)
        entry_responsavel.insert(0, tarefa[5])
        entry_responsavel.grid(row=5, column=1)

        # Botão para salvar alterações
        btn_salvar = tk.Button(janela_editar, text="Salvar", command=salvar_alteracao)
        btn_salvar.grid(row=6, columnspan=2)
    else:
        messagebox.showerror("Erro", "Selecione uma tarefa para alterar.")

# Interface gráfica com Tkinter
root = tk.Tk()
root.title("CRUD de Tarefas")

# Campo de pesquisa
tk.Label(root, text="Pesquisar por Nome:").grid(row=0, column=0, padx=10, pady=10)
entry_pesquisa = tk.Entry(root)
entry_pesquisa.grid(row=0, column=1, padx=10, pady=10)
entry_pesquisa.bind("<KeyRelease>", lambda event: atualizar_lista(entry_pesquisa.get()))

# Botões
btn_adicionar = tk.Button(root, text="Adicionar", command=adicionar_tarefa)
btn_adicionar.grid(row=0, column=2, padx=10, pady=10)

btn_alterar = tk.Button(root, text="Alterar", command=alterar_tarefa)
btn_alterar.grid(row=0, column=3, padx=10, pady=10)

btn_deletar = tk.Button(root, text="Deletar", command=deletar_tarefa)
btn_deletar.grid(row=0, column=4, padx=10, pady=10)

# Grid (Treeview) para exibir a lista de tarefas
tree = ttk.Treeview(root, columns=("ID", "Nome", "Descrição", "Tempo", "Status", "Responsavel", "Importante"), show="headings")
tree.heading("ID", text="Número da Tarefa")
tree.heading("Nome", text="Nome")
tree.heading("Descrição", text="Descrição")
tree.heading("Tempo", text="Tempo")
tree.heading("Status", text="Status")
tree.heading("Responsavel", text="Responsável")
tree.heading("Importante", text="Importante")

tree.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

# Atualiza o grid inicialmente
atualizar_lista()

# Executa a interface
root.mainloop()

# Fechar a conexão com o banco de dados ao encerrar o programa
conexao.close()
