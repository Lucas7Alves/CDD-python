nomes = [""]*4
tam = len(nomes)
for i in range(tam):
    nomes[i] = input(f"Digite o {i+1}° nome: ")
for j in range(tam):
    print(nomes[j], end = "\n")

print("Agora no inverso: ")

for k in range(tam-1, -1, -1):
    print(nomes[k], end = "\n")