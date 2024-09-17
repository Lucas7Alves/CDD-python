num = int(input("Digite um número: "))

for i in range(num+1):
    for j in range(i):
        print(j, end=" ")
    print()

