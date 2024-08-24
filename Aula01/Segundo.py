while True:
    
    nome = input("Digite um nome ('sair para sair): ")

    # lower é usado para converter todas as letras para minusculo.
    # if nome.lower() == "sair":

    # Upper é usado para converter todas as letras para maiusculo.
    if nome.upper() == "SAIR":
        break

    for letra in nome:
        print(letra)

print("Bye")
