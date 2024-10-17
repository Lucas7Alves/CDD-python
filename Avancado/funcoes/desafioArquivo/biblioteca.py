
def appendArq(txt):
    with open("../../TurmaC.txt", "a") as arq:
        arq.write(f"\n{txt}")

def reading():
    with open("../../TurmaC.txt", "r") as arqLer:
        print(arqLer.read())
def search(txt):
    with open("../../TurmaC.txt", "r") as arqLer:

        cont = 0
        for x in arqLer:
            if x in txt:
                cont += 1
        print(f"Há {cont} ocorrencias de {txt}")