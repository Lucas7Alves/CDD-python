a = [0]*5
ln = len(a)

for i in range(ln):
    a[i] = int(input("Digite um número: "))

for x in range((ln-1),-1,-1):
    print(a[x])