num1 = int(input("Digite o 1° número: "))
num2 = int(input("Digite o 2° número: "))


if num1 > num2:
    print(f"{num2}, {num1}")
elif num1 == num2:
    print("São enguais!")
else:
    print(f"{num1}, {num2}")

