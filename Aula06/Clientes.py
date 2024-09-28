

print('Cadastro de clientes')
print('Desenvolvido por Victor Santarossa')
print('Versão 1.0')
print('__________________________________')

def formataData(data):
    novaData  = data[0] + data[1] + '/' 
    novaData += data[2] + data[3] + '/' 
    novaData += data[4] + data[5] + data[6] + data[7]
    return novaData

nome =       input('Nome do Cliente : ')
cpf =        input('CPF             : ')
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

print(cliente.items()  )
print(cliente.keys()   )
print(cliente.values() )