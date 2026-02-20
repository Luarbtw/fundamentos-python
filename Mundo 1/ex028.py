#jogo da adivinhação
from random import choice as ch

print ('---- Vou pensar em um número de 0 a 5, tente advinhar ----')

n = [0, 1, 2, 3, 4, 5]

random_n = ch(n)

guess = int(input('Qual número eu pensei? '))

if 0 <= guess <= 5: #verifica se o número está entre 0 e 5
    if guess == random_n:
        print(f'Você acertou! O número que pensei é {random_n}')
    else: 
        print(f'Você errou! O número que pensei é {random_n}')
else:
    print('Esse número nem está entre 0 e 5 kkkk')
