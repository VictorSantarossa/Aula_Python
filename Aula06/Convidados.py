#Montar um sistema utilizando print e input que peça para digitar o nome de pessoas,
#uma de cada vez, e adicioná-los em um lista chamada listaConvidados.
#Quando o usuário apertar o enter sem ter digitado um nome, o sistema irá listar
#os nomes que forem cadastrados.
listaConvidados = []

while True:
    nome = input("Digite o nome do iconvdado: ")
    if nome == '':
        break
    listaConvidados.append(nome)

for convidado in listaConvidados:
    print(convidado)