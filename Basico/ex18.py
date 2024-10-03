totalAlunos = int(input("Digite o total de alunos: "))
notas = 0
x = 1
while x <= totalAlunos:
    notas += int(input("Digite a nota dos alunos: "))
    x += 1
mediaAritimetica = notas/totalAlunos

print(f"A média da turma: {mediaAritimetica:.2f}")