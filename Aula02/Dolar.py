#Montar um sistema que converta Dolar ou Euro para Real:

#Converter Dolar->Real = Multiplica o preço em Dolar pela cotação do Dolar
#Converter Euro->Real = Multiplica o preço em Euro pela cotação do Euro

#Pedir:
#- O valor do produto em Dolar ou Euro
#- A Cotação do Dolar ou do Euro
#- Calcular o valor em Real
#- Mostrar o valor calculado na tela

def main():
    converter = int(input("\nDigite [1] para converter de Dólar para Real ou [2] para converter de Euro para Real: "))

    if converter == 1:
        valor = float(input("\nDigite o valor em dólares: "))
        cotacao_dolar = 5.49
        Real = cotacao_dolar * valor
        print(f"${valor:.2f} convertido para Real é: R${Real:.2f}")
    
    elif converter == 2:
        valor = float(input("\nDigite o valor em euros: "))
        cotacao_euro = 6.15
        Real = cotacao_euro * valor
        print(f"€{valor:.2f} convertido para Real é: R${Real:.2f}")
    
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")