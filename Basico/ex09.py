litros = float(input("Quantos litros foi colocado? "))
tipoCombustivel = input("Digite o tipo do combustível: ")
valorTotal = 0

if tipoCombustivel == "g":
    valorTotal = litros * 5.80
else:
    valorTotal = litros * 4.90
print(f"O valor da conta foi de {valorTotal:.2f}R$")
