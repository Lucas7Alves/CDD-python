def imprimirNome(nome):
    print(f"{nome}")

def piramide(num):
    for x in range(1, num+1):
        for y in range(x):
            print(x, end = " ")
        print()