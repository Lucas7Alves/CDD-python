cont = 1
sum=0
while cont <= 10:
    res = int(input(f"Digite o {cont} valor: "))
    sum += res
    cont += 1

media = sum / cont
print(media)

