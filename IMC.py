while True:

    peso = float(input("Digite seu peso (0 para sair): "))
    if peso == 0:
        break
    altura = float(input("Digite sua altura: "))
    imc = peso / (altura*altura)

    if imc > 40:
        print(f"Seu IMC é: {imc:.2f} = Obesidade grau 3")
    elif imc > 35:
        print(f"Seu IMC é: {imc:.2f} = Obesidade grau 2")
    elif imc > 30:
        print(f"Seu IMC é: {imc:.2f} = Obesidade grau 1")
    elif imc > 25:
        print(f"Seu IMC é: {imc:.2f} = Sobrepeso")
    elif imc > 18.5:
        print(f"Seu IMC é: {imc:.2f} = Peso normal")
    else:
        print(f"Seu IMC é: {imc:.2f} = Baixo peso")

    print("Teste")