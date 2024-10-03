from re import match

num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
opcao = 0
soma = 0
while opcao != 6:
    print("1. Somar")
    print("2. Subtração")
    print("3. Multiplicar")
    print("4. Divisão")
    print("5. Novo número")
    print("6. Sair")

    match opcao:
        case 1:
            soma = num1 + num2
            print(soma)
            break
        case 2:
            soma = num1 - num2
            print(soma)
            break
        case 3:
            soma = num1 * num2
            print(soma)
            break
        case 4:
            soma = num1 / num2
            print(soma)
            break
        case 5:
            continue
        case 6:
            break
