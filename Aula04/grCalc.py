import tkinter as tk
from tkinter import messagebox

def Somar():
    try:
    
        num1 = float(entryNum1.get())
        num2 = float(entryNum2.get())
        
        result = num1 + num2
        
        messagebox.showinfo("Cálculo Realizado Com Sucesso", f"O resultado é: {result:.2f}")
    except ValueError:
       
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

def Subtrair():
    try:
    
        num1 = float(entryNum1.get())
        num2 = float(entryNum2.get())
        
        result = num1 - num2
        
        messagebox.showinfo("Cálculo Realizado Com Sucesso", f"O resultado é: {result:.2f}")
    except ValueError:
       
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

def Multiplicar():
    try:
    
        num1 = float(entryNum1.get())
        num2 = float(entryNum2.get())
        
        result = num1 * num2
        
        messagebox.showinfo("Cálculo Realizado Com Sucesso", f"O resultado é: {result:.2f}")
    except ValueError:
       
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

def Dividir():
    try:
        num1 = float(entryNum1.get())
        num2 = float(entryNum2.get())
        
        if num2 == 0:
            messagebox.showerror("Erro", "Não é possível dividir por zero.")
            return
        
        result = num1 / num2
        
        messagebox.showinfo("Cálculo Realizado Com Sucesso", f"O resultado é: {result:.2f}")
    except ValueError:
        
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

windows = tk.Tk()
windows.title("CalculoDoDia")
windows.geometry("800x600")
windows.config(bg="black")

labelNum1 = tk.Label(windows, text="Digite o primeiro número: ",width=20, font=("Arial", 16, "bold"), fg="gray", bg="black")
labelNum1.pack(padx=10,pady=5)

entryNum1 = tk.Entry(windows,width=58)
entryNum1.pack(padx=10,pady=5)

labelNum2 = tk.Label(windows, text="Digite o segundo número: ",width=20, font=("Arial", 16, "bold"), fg="gray", bg="black")
labelNum2.pack(padx=10,pady=5)

entryNum2 = tk.Entry(windows,width=58)
entryNum2.pack(padx=10,pady=5)

button_Acao = tk.Button(windows, text="Somar", command = Somar,width=20, font=("Arial", 14, "bold"), fg="black", bg="grey")
button_Acao.pack(ipadx= 50, pady= 20)

button_Acao = tk.Button(windows, text="Subtrair", command = Subtrair,width=20, font=("Arial", 14, "bold"), fg="black", bg="grey")
button_Acao.pack(ipadx= 50, pady= 20)

button_Acao = tk.Button(windows, text="Multiplicar", command = Multiplicar,width=20, font=("Arial", 14, "bold"), fg="black", bg="grey")
button_Acao.pack(ipadx= 50, pady= 20)

button_Acao = tk.Button(windows, text="Dividir", command = Dividir,width=20, font=("Arial", 14, "bold"), fg="black", bg="grey")
button_Acao.pack(ipadx= 50, pady= 20)

windows.mainloop()