#Montar um codigo em python onde o usuario tera que adivinhar um numero.
#O sistema mostrá as seguintes frases.
#"Você Chutou baixo" - se o numero que a pessa digitou for menor que o número escolhido.
#"Você Chutou alto" - se o numero que a pessa digitou for maior que o número escolhido.
#"Você acertou" - se o numero que a pessa digitou for igual ao número escolhido.

import random
numGerado = random.randint(1, 100)
tentativa = 0

while True:
    num = int(input("Digite um numero de 0 a 100 para tentar acertar: "))
    if num < numGerado:
        tentativa += 1
        print("\n!!!Você Chutou baixo!!!")
    elif num > numGerado:
        tentativa += 1
        print("\n!!!Você Chutou alto!!!")
    elif num == numGerado:
        tentativa += 1
        print("\n!!!Parabéns Você acertou, e teve um total de :",tentativa,"Tentativas!!!")
        break
    