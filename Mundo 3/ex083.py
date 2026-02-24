lista = []

expressao = str(input("Digite a expressão: ")) 

for caractere in expressao:
    if caractere == "(":
        lista.append("(")
    elif caractere == ")":
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append("x")
            break

if len(lista) == 0:
    print("Correto")
else:
    print("Incorreto")

