num = [0]*4
tam = len(num)

for i in range(tam):
    num[i] = int(input("Digite um número: "))

for j in range(tam):
    if num[j] %2 == 0:
        print(f"{num[j]} é par", end = " ")
minimo = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000
maxim = -10000000000000000000000000000000000000000000000000000000000000000000000000000000000
print()
for k in range(tam):
    if num[k] > maxim:
        maxim = num[k]
for l in range(tam):
    if num[l] < minimo:
        minimo = num[l]

print(f"O valor minimo é {minimo} e o máximo é {maxim}")
soma = 0
for m in range(tam):
    soma += num[m]
media = soma/5
for n in range(tam):
    if num[n] > media:
        print(f"O valor {num[n]} está acima da média")