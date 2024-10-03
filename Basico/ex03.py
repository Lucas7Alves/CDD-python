name = input("Digite seu nome: ")
idade = input("Digite seu idade: ")
sal = float(input("Digite seu salário: "))

idadeNova = int(idade) * 12
sal = sal * 1.10

print(f"Olá {name}, que bom que você tem {idade} anos! E se fosse em meses {idadeNova} meses!! E seu salário é {sal:.2f}!!")