def par(n):
    if n %2 == 0:
        print(f"{n} é par")

def impar(n):
    if n %2 != 0:
        print(f"{n} é ímpar")

def contarVogais(txt):
    cont = 0
    t = len(txt)
    for x in range(t):
        if txt[x] in "aeiou":
            cont +=1
    print(f"Encontramos {cont}")


def soma(num1,num2,num3,num4,num5):
    sum = num1+num2+num3+num4+num5
    print(sum)


def somar(*numeros):
    sum = 0
    for i in range(len(numeros)):
        sum += numeros[i]
    return print(sum)

def contarTexto(txt):
    t = len(txt)
    tot = t
    for i in range(t):
        if txt[i] == " ":
            tot -= 1
    print(tot)
    for j in range(t-1, -1, -1):
        print(txt[j], end= "")

def noRepeat(num):

    newList = []
    for i in num:
        if i not in newList:
            newList.append(i)
    print(newList)

def ehPrimo(num):
    if num == 1 or num == 2:
        print("1 e 2 não conta!")
    for i in range(2,num):
        if num%i == 0:
            return num," Não é primo"
    return num, " É primo"