p1 = int(input("Qual o primeiro termo da sua PA?: "))
r = int(input("Qual a razão da sua PA?: "))
contador = 10

print(f"Os primeiros 10 termos de uma PA que começa com {p1} e tem razão {r} é: ")

while contador >= 1:
    print(f"{p1} -> ", end='')
    contador -= 1
    p1 += r
print("FIM")

    

