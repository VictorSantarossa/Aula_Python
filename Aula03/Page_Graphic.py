# O "as" em frente ao import é usado para apelidar a biblioteca.
import tkinter as tk
from tkinter import messagebox

def click():
    messagebox.showinfo("Boas Vindas",f"Bom dia, {entryNome.get()}")

janela = tk.Tk()
janela.geometry("400x300")
janela.title("Aula03_Python")

labelNome = tk.Label(janela,text = "Digite seu nome:")
labelNome.pack(ipadx = 10, pady = 20)

entryNome = tk.Entry(janela)
entryNome.pack(ipadx= 40, pady= 5)

button_First = tk.Button(janela, text="Clique Aqui", command = click)
button_First.pack(ipadx= 50, pady= 5)

janela.mainloop()