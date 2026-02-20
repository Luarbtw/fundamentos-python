from random import randint

contador = 0

while True:
    print("="*30)
    print("Vamos jogar ímpar ou par")
    print("="*30)

    player = int(input("Diga um valor: "))
    cpu = randint(0, 10)
    total = (player + cpu) % 2

    escolha = str(input("Par ou ímpar? [P/I]: ")).upper().strip()

    print("~"*30)
    print(f"Você escolheu {player} e eu escolhi {cpu}, totalizando {player + cpu}.", end='')

    if escolha == 'P' and total == 0:
        print(" Deu PAR, você venceu!")
        contador += 1
    elif escolha == 'I' and total != 0:
        print(" Deu IMPAR, você venceu!")
        contador += 1

    elif escolha == 'P' and total != 0:
        print(" Deu IMPAR, eu ganhei!")
        break

    elif escolha == 'I' and total == 0:
        print(" Deu PAR, eu ganhei!")
        break
    
print("-"*40)
print(f"GAME OVER! você acertou {contador} vezes até perder.")
print("-"*40)       


   
