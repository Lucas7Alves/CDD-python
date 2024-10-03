num1 = float(input("Digite a nota 1: "))
num2 = float(input("Digite a nota 2: "))
num3 = float(input("Digite a nota 3: "))

media = (num1+num2+num3) / 3

if media >= 7.0:
    print("Aprovado!")
elif media < 4:
    print("Reprovado!")
else:
    print("Recuperação")
