user = [""]*5
pw = [""]*5
tam = len(user)
for i in range(tam):
    user[i] = input("Digite o seu user: ")
    pw[i] = input("Digite sua senha: ")

for j in range(tam):
    print(f"O usuário {user[j]} tem a senha {pw[j]} na posição {j+1}°")