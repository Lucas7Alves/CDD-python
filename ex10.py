res = int(input("Digite o um número de 1 a 12: "))

if res < 1 or res > 12:
    print("Numéro inválido!!")
elif res == 2:
    print("Fev")
elif res == 3:
    print("Mar")
elif res == 4:
    print("Abr")
elif res == 5:
    print("Mai")
elif res == 6:
    print("Jun")
elif res == 7:
    print("Jul")
elif res == 8:
    print("Ago")
elif res == 9:
    print("Set")
elif res == 10:
    print("Out")
elif res == 11:
    print("Nov")
elif res == 12:
    print("Dez")
else:
    print("Jan")