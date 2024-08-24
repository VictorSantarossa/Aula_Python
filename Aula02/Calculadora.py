print(" ________________________________________")
print("|CyberCalc - Sistema de operações simples|")
print("|Desenvolvido por: Victor santarossa     |")
print("|Criado em 24/08/2024                    |")
print("|Versão 1.0                              |")
print("|________________________________________|")

def entrada1():
    while True:  
        entrada = input("\nDigite o primeiro valor: ")
        try:
            num = float(entrada)
            return num
        except ValueError:
            print("Erro: valor inválido. Por favor, digite um número válido.")

def entrada2():
    while True:
        entrada = input("\nDigite o segundo valor: ")
        try:
            num = float(entrada)
            return num
        except ValueError:
            print("Erro: valor inválido. Por favor, digite um número válido.")

def calcular(num1, num2, operacao):
    if operacao == "1":
        return num1 + num2
    elif operacao == "2":
        return num1 - num2
    elif operacao == "3":
        if num2 == 0:
            return "Erro: divisão por zero."
        return num1 / num2
    elif operacao == "4":
        return num1 * num2
    else:
        return "Operação inválida."

num1 = entrada1()
num2 = entrada2()

calculo = input("\nDigite 1 = +"
                "\nDigite 2 = -"
                "\nDigite 3 = /"
                "\nDigite 4 = *"
                "\n\nSelecione qual o cálculo que deseja: ")

resultado = calcular(num1, num2, calculo)
print(f"\nO cálculo entre {num1} e {num2} é: {resultado}")