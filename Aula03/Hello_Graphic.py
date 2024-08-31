# O "as" em frente ao import é usado para apelidar a biblioteca.
import tkinter as tk

janela = tk.Tk()
janela.geometry("400x300")
janela.title("Aula03_Python")

labelNome = tk.Label(janela,text = "Digite seu nome:")
labelNome.pack(padx = 10, pady = 20)

janela.mainloop()