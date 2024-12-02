def exibir_menu():
    print("\n============ MENU ============")
    print("1. Exibir Lista De Funcionário")
    print("2. Adicionar Funcionário      ")
    print("3. Remover Funcionário        ")
    print("4. Alterar Funcionário        ")
    print("5. Sair                       ")
    print("==============================")

def exibir_funcionario(funcionarios):
    if not funcionarios:
        print("Nenhum funcionário cadastrado.")
    else:
        print("\nFuncionários cadastrados:")
        for codigo, dados in funcionarios.items():
            print(f"ID: {codigo} | Nome: {dados['nome']} | Cargo: {dados['cargo']} | Salário: R${float(dados['salario']):.2f}")

def adicionar_funcionario(funcionarios):
    codigoFuncionario = input("Digite o código para adicionar: ")
    if codigoFuncionario in funcionarios:
        print("Código já existente. Tente novamente.")
        return

    nomeFuncionario = input("Digite o nome do funcionário: ")
    cargoFuncionario = input("Digite o cargo do funcionário: ")
    try:
        salarioFuncionario = float(input("Digite o salário do funcionário: "))
    except ValueError:
        print("Salário inválido. Tente novamente.")
        return

    funcionarios[codigoFuncionario] = {"nome": nomeFuncionario,
                                       "cargo": cargoFuncionario,
                                       "salario": salarioFuncionario}

    print(f"'{nomeFuncionario}' foi adicionado à lista.")

def remover_funcionario(funcionarios):
    codigoFuncionario = input("Digite o código do funcionário a ser removido: ")
    if codigoFuncionario in funcionarios:
        funcionario = funcionarios.pop(codigoFuncionario)
        print(f"'{funcionario['nome']}' foi removido com sucesso.")
    else:
        print("Código não encontrado. Nenhum funcionário removido.")

def alterar_funcionario(funcionarios):
    codigoFuncionario = input("Digite o código do funcionário a ser alterado: ")
    if codigoFuncionario in funcionarios:
        print("\nO que você deseja alterar?")
        print("1. Nome")
        print("2. Cargo")
        print("3. Salário")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            novo_nome = input("Digite o novo nome: ")
            funcionarios[codigoFuncionario]["nome"] = novo_nome
            print("Nome alterado com sucesso.")
        elif opcao == "2":
            novo_cargo = input("Digite o novo cargo: ")
            funcionarios[codigoFuncionario]["cargo"] = novo_cargo
            print("Cargo alterado com sucesso.")
        elif opcao == "3":
            try:
                novo_salario = float(input("Digite o novo salário: "))
                funcionarios[codigoFuncionario]["salario"] = novo_salario
                print("Salário alterado com sucesso.")
            except ValueError:
                print("Salário inválido. Alteração não realizada.")
        else:
            print("Opção inválida. Nenhuma alteração foi feita.")
    else:
        print("Código não encontrado. Nenhuma alteração foi realizada.")

def main():
    funcionarios = {}
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção:")

        if opcao == "1":
            exibir_funcionario(funcionarios)
        elif opcao == "2":
            adicionar_funcionario(funcionarios)
        elif opcao == "3":
            remover_funcionario(funcionarios)
        elif opcao == "4":
            alterar_funcionario(funcionarios)
        elif opcao == "5":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
