from biblioteca import *

while True:
    opcao = int(input("O que deseja fazer: "))

    match opcao:
        case 1:
            appendArq(input("Digite o nome para adicionar ao arquivo"))
        case 2:
            reading()
        case 3:
            pass
        case 4:
            break
        case _:
            print("Opção inválida")