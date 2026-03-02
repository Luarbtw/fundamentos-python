from random import choice
from time import sleep
lista = []
jogo = []

print("-"*30)
print("          MEGA SENA         ")
print("-"*30)

jogos = int(input("Quantos jogos você quer?: "))

print(f"------ Sorteando {jogos} jogos... ------")

for i in range(jogos):

    while len(jogo) < 6:
        x = choice(range(1, 61))
        if x not in jogo:
            jogo.append(x)
            
    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()

    print(f"JOGO {i+1}: {lista[i]}")
    sleep(1)

print("BOA SORTE!")
    

