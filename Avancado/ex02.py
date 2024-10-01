from operator import length_hint

arrayAlunos = [""]*5
length = len(arrayAlunos)

for x in range(length):
    arrayAlunos[x] = input("Digite o nome do aluno: ")

for i in arrayAlunos:
    print(i)