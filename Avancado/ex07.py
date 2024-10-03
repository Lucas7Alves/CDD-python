num = [0]*10
tam = len(num)
for i in range(tam):
    num[i] = int(input("Digite um número: "))

x = int(input("Digite um número para verificar se existe no array: "))
cont = 0
for j in range(tam):
    if x == num[j]:
        cont += 1

print(f"Existe {cont} no {x} no array")