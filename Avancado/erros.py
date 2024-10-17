try :
    a = 0 / 0
    print(a)
except ZeroDivisionError:
    print("Não pode divisão por zero")
try:
    print(x)
except NameError:
    print(f"A variável x não existe")

try:
    print(f"{"a"-3}")
except TypeError:
    print("Tipos diferente")
print("Terminou")

try:
    b = [0]
    for i in b:
        print(b[i+4])

except IndexError:
    print("Deu erro no index")

