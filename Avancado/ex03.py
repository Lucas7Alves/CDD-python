notas = [""]*5
ln = len(notas)
for i in range(ln):
    notas[i] = float(input(f"Digite a nota do {i+1}° aluno: "))
media = 0
for i in range(ln):
    media += notas[i]
totMedia = media/5
cont = 0
for i in range(ln):
    if notas[i] > totMedia:
        cont += 1
print(cont)