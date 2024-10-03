res=0
sum=0
for i in range(1,11):
    res = int(input(f"Digite o número {i}: "))

    if res %2 != 0:
        sum += res
    elif res == 1:
        sum += res
print(f"A soma dos números ímpares é: {sum}")
