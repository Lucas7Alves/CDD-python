res = 1
while res == 1:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    while num2 == 0:
        print("\nDigite um número diferente de 0")
        num2 = int(input("Digite o segundo número: "))
    div = num1 / num2
    print(f"O resultado é: {div}")
    print("Deseja repetir a operação?")
    res = int(input("Digite 1 para Sim, 2 para não: "))
print("Fim do programa!!")