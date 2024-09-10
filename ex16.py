totalAlunos = int(input("Digite o total de alunos: "))
notas = 0
for i in range(totalAlunos):
    notas += int(input("Digite a nota dos alunos: "))
mediaAritimetica = notas/totalAlunos

print(f"A média da turma: {mediaAritimetica}")