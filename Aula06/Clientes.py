print('Cadastro de clientes')
print('Desenvolvido por Victor Santarossa')
print('Versão 1.0')
print('__________________________________')

def formataData(data):
    novaData  = data[0] + data[1] + '/' 
    novaData += data[2] + data[3] + '/' 
    novaData += data[4] + data[5] + data[6] + data[7]
    return novaData

def formataCPF(cpf):
    novoCPF  = cpf[0] + cpf[1] + cpf[2] + '.'
    novoCPF += cpf[3] + cpf[4] + cpf[5] + '.'
    novoCPF += cpf[6] + cpf[7] + cpf[8] + '-'
    novoCPF += cpf[9] + cpf[10]
    return novoCPF

nome =       input('Nome do Cliente : ')
cpf =        input('CPF             : ')
cpf =        formataCPF(cpf)
nascimento = input('Nascimento      : ')
nascimento = formataData(nascimento)
logradouro = input('Logradouro      : ')
numCasa =    input('Número          : ')
bairro =     input('Bairro          : ')
cidade =     input('Cidade          : ')
estado =     input('Estado          : ')

cliente = {
    'nome'       : nome,
    'cpf'        : cpf,
    'nascimento' : nascimento,
    'logradouro' : logradouro,
    'numCasa'    : numCasa,
    'bairro'     : bairro,
    'cidade'     : cidade,
    'estado'     : estado
}

# Mostra os itens do dicionário cliente
print(cliente.items())

# Mostra as chaves do dicionário cliente
print(cliente.keys())

# Mostra os valores do dicionário cliente
print(cliente.values())
