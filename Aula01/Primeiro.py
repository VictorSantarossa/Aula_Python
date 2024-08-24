ContarAte = 1
while ContarAte > 0:
    ContarAte = int(input("Deseja contar ate: (0 parar sair):"))
    # if ContarAte == 0:
    #     break
    for contador in range(ContarAte):
        print(contador+1)
print("Encerrado!")