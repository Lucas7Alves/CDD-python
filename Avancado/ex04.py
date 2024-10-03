a = [0]*10
m = [0]*10
ln = len(a)

for i in range(ln):
    a[i] = int(input("Digite um número: "))
x = int(input("Digite o multiplicador: "))

for x in range(ln):
    m[x] = a[x] * x

print(m)
