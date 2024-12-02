def exibir_menu():
    print("\n==== MENU =====")
    print("1. Exibir Lista  ")
    print("2. Adicionar Item")
    print("3. Romover Item  ")
    print("4. Alterar Item  ")
    print("5. Sair          ")
    print("=================")

def exibir_lista(lista):
    if not lista:
        print("A Lista está vazia.")
    else:
        print("\nLista Atual:")
        for i, item in enumerate(lista, start=1):
            print(f"{i}. {item}")

def adicionar_item(lista):
    item = input("Digite o item para adicionar: ")
    lista.append(item)
    print(f"'{item}'foi Adicionado à lista.")

def remover_item(lista):
    exibir_lista(lista)
    if lista:
        try:
            indice = int(input("Digite o número do item para remover: "))
            if 1<= indice <= len (lista):
                removido = lista.pop(indice - 1)
                print(f"'{removido}'foi removido da lista.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Por favor, digite um número vàlido.")

def alterar_item(lista):
    exibir_lista(lista)
    if lista:
        try:
            indice = int(input("Digite o número do item para alterar: "))
            if 1 <= indice <= len(lista):
                novo_valor = input("Digite o novo valor: ")
                antigo_valor = lista[indice - 1]
                lista[indice - 1] = novo_valor
                print(f"'{antigo_valor}' foi alterado para '{novo_valor}'.")
            else:
                print("Número Inválido.")
        except ValueError:
            print("Por favor, digite um número válido.")

def main():
    lista = []
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção:")

        if opcao == "1":
            exibir_lista(lista)
        elif opcao == "2":
            adicionar_item(lista)
        elif opcao == "3":
            remover_item(lista)
        elif opcao == "4":
            alterar_item(lista)
        elif opcao == "5":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()