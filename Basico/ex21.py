res = 1
while res == 1:
    cont = 0
    num = int(input("Digite um número: "))
    while cont <= 10:
        print(f"{num} X {cont} = {num*cont}")
        cont += 1
    res = int(input("Deseja repetir a operação?\n"
                    "Resposta: "))