time1 = input("Time um: ")
gols1 = int(input("Digite quantos gols esse time fez? "))

time2 = input("Time dois: ")
gols2 = int(input("Digite quantos gols esse time fez? "))

if gols1 > gols2:
    print(f"Time do {time1} venceu o time {time2} por {gols1} a {gols2}!!")
elif gols2 > gols1:
    print(f"Time do {time2} venceu o time {time1} por {gols2} a {gols1}!!")
else:
    print("Deu empate!!!")