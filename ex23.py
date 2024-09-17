res = 1
while res == 1:
    nota1 = float(input("Digite a primeira nota: "))

    while nota1 < 0 or nota1 > 10:
        print("Só é válido notas de 0 a 10!")
        nota1 = float(input("Digite a primeira nota: "))

    nota2 = float(input("Digite a segunda nota: "))

    while nota2 < 0 or nota2 > 10:
        print("Só é válido notas de 0 a 10!")
        nota2 = float(input("Digite a primeira nota: "))
    media = (nota1+nota2)/2
    print(media)
    res = int(input("Deseja realizar um novo cálculo? (0 para não / 1 para sim): "))
