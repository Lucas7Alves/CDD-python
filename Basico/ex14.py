res = int(input("Digite um número: "))

for i in range(res+1):
    if i %2 != 0:
        print(f"{i} é impar")
    elif i == 1:
        print(f"{i} é impar")