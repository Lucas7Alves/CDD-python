arrayAlunos = [""]*5
length = len(arrayAlunos)

for x in range(length):
    arrayAlunos[x] = input("Digite o nome do aluno: ")

for i in range(length):
    print(f"{arrayAlunos[i]} está na posição {i}")