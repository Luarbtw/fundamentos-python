p1 = int(input("Qual o primeiro termo da sua PA?: "))
r = int(input("Qual a razão da sua PA?: "))
contador = 0
total = 0
limite = 10

print(f"Os primeiros 10 termos de uma PA que começa com {p1} e tem razão {r} é: ")

while contador < limite:
    print(f"{p1} -> ", end='')
    p1 += r

    contador += 1
    total += 1
    

    if contador == limite:
        print("PAUSA")
        continuador = int(input("Quantos termos você quer mostrar a mais? "))
        limite += continuador   

        if continuador == 0:
            contador = limite
            print("Programa encerrado.")

print(f"Foram mostrados {total} termos da PA.")

    
    


