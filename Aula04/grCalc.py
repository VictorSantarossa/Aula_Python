import tkinter as tk
from tkinter import messagebox

def click():
    result = entryNum1 + entryNum2
    messagebox.showinfo("Calculo Realizado Com Sucesso",result)

windows = tk.Tk()
windows.title("CalculoDoDia")
windows.geometry("800x600")
windows.config(bg="black")

labelNum1 = tk.Label(windows, text="Digite o primeiro número: ")
labelNum1.pack(padx=10,pady=5)

entryNum1 = tk.Entry(windows)
entryNum1.pack(padx=10,pady=5)

labelNum2 = tk.Label(windows, text="Digite o segundo número: ")
labelNum2.pack(padx=10,pady=5)

entryNum2 = tk.Entry(windows)
entryNum2.pack(padx=10,pady=5)

button_Somar = tk.Button(windows, text="Somar", command = click, font=("Arial", 14, "bold"), fg="black", bg="grey")
button_Somar.pack(ipadx= 50, pady= 20)

windows.mainloop()