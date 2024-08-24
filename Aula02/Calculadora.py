def entrada_valida(mensagem):
    while True:
        entrada = input(mensagem)
        try:
            return float(entrada)
        except ValueError:
            print("Erro: valor inválido. Por favor, digite um número válido.")

def obter_operacao_valida():
    while True:
        operacao = input("\n ____________"
                         "\n|Digite 1 = +|"
                         "\n|Digite 2 = -|"
                         "\n|Digite 3 = /|"
                         "\n|Digite 4 = *|"
                         "\n|____________|"
                         "\n\nSelecione qual o cálculo que deseja: ")
        if operacao in ["1", "2", "3", "4"]:
            return operacao
        print("Operação inválida. Por favor, digite um número entre 1 e 4.")

def calcular(num1, num2, operacao):
    if operacao == "1":
        return num1 + num2
    elif operacao == "2":
        return num1 - num2
    elif operacao == "3":
        if num2 == 0:
            return "\nErro: divisão por zero."
        return num1 / num2
    elif operacao == "4":
        return num1 * num2
    else:
        return "Operação inválida."

print(" ________________________________________")
print("|CyberCalc - Sistema de operações simples|")
print("|Desenvolvido por: Victor Santarossa     |")
print("|Criado em 24/08/2024                    |")
print("|Versão 1.0                              |")
print("|________________________________________|")

realizar = input("\nDigite [1] para CONTINUAR ou [2] para SAIR: ")

while realizar == "1":
    num1 = entrada_valida("\nDigite o primeiro valor: ")
    num2 = entrada_valida("\nDigite o segundo valor: ")

    operacao = obter_operacao_valida()

    resultado = calcular(num1, num2, operacao)
    print(f"\nO cálculo entre {num1} e {num2} é: {resultado}")

    realizar = input("\nDigite [1] para CONTINUAR ou [2] para SAIR: ")
