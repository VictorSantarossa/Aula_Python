# O "as" em frente ao import é usado para apelidar a biblioteca.
import tkinter as tk

janela = tk.Tk()
janela.geometry("800x600")
janela.title("Aula03_Python")

labelNome = tk.Label(janela,text = "Digite seu nome:")
labelNome.pack(padx = 10, pady = 20)

entryNome = tk.Entry(janela, width=50)
entryNome.pack(padx= 10, pady= 5)

buttonHello = tk.Button(janela, text="Clique Aqui")
buttonHello.pack(padx= 10,pady= 30)

janela.mainloop()