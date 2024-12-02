import tkinter as tk
from tkinter import messagebox
import requests

def Buscar():
    cep = entry_CEP.get().strip()
    
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        
        if "erro" in dados:
            messagebox.showerror("Erro", "CEP não encontrado.")
        else:
            entry_Logradouro.delete(0,tk.END)
            entry_Logradouro.insert(0,dados['logradouro'])

            entry_Bairro.delete(0,tk.END)
            entry_Bairro.insert(0,dados['bairro'])

            entry_Cidade.delete(0,tk.END)
            entry_Cidade.insert(0,dados['localidade'])

            entry_Estado.delete(0,tk.END)
            entry_Estado.insert(0,dados['uf'])
            
    else:
        messagebox.showerror("Erro", "Erro na consulta ao ViaCEP.")


windows = tk.Tk()
windows.title("Busca CEP")
windows.geometry("600x320")

label_CEP = tk.Label(windows, text = "CEP")
label_CEP.grid(column = 0, row = 0, sticky="w", padx = 5, pady = 5)
entry_CEP = tk.Entry(windows)
entry_CEP.grid(column = 1, row = 0, padx = 5, pady = 5)

label_Logradouro = tk.Label(windows, text = "Logradouro")
label_Logradouro.grid(column = 0, row = 1, sticky="w", padx = 5, pady = 5)
entry_Logradouro = tk.Entry(windows)
entry_Logradouro.grid(column = 1, row = 1, padx = 5, pady = 5)

label_Bairro = tk.Label(windows, text = "Bairro")
label_Bairro.grid(column = 0, row = 2, sticky="w", padx = 5, pady = 5)
entry_Bairro = tk.Entry(windows)
entry_Bairro.grid(column = 1, row = 2, padx = 5, pady = 5)

label_Cidade = tk.Label(windows, text = "Cidade")
label_Cidade.grid(column = 0, row = 3, sticky="w",  padx = 5, pady = 5)
entry_Cidade = tk.Entry(windows)
entry_Cidade.grid(column = 1, row = 3, padx = 5, pady = 5)

label_Estado= tk.Label(windows, text = "Estado")
label_Estado.grid(column = 0, row = 4, sticky="w", padx = 5, pady = 5)
entry_Estado = tk.Entry(windows)
entry_Estado.grid(column = 1, row = 4, padx = 5, pady = 5)

button1 = tk.Button(windows, text = "Buscar", command = Buscar, width = 20, font =("Arial", 12,"bold"))
button1.grid(column = 2, row = 0, padx = 5, pady = 5)


windows.mainloop()