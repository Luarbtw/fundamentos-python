from time import sleep
from random import choice

print('Bora jogar pedra papel tesoura!')
print('-' * 15)
print('[ 1 ] PEDRA \n[ 2 ] PAPEL \n[ 3 ] TESOURA')
print('-' * 15)

escolha = int(input('Escolha sua jogada! '))

options = [ 'PEDRA', 'PAPEL', 'TESOURA' ]

escolhacpu = choice(options)

print('JO', end = '')

sleep(1)

print('KEN', end = '')

sleep(1)

print('PO!')

if escolha == 1:
    escolha = 'PEDRA'

    print('-=' * 10)
    print(f'VOCÊ ESCOLHEU {escolha} \nEU ESCOLHI {escolhacpu}')
    print('-=' * 10)

    sleep(1)
    if escolha == escolhacpu:
        print('EMPATE!')

    elif escolhacpu == 'PAPEL':
        print('VOCÊ PERDEU!')

    elif escolhacpu == 'TESOURA':
        print('VOCÊ GANHOU!')

elif escolha == 2:
    escolha = 'PAPEL'

    print('-=' * 10)
    print(f'VOCÊ ESCOLHEU {escolha} \nEU ESCOLHI {escolhacpu}!')
    print('-=' * 10)

    sleep(1)
    if escolha == escolhacpu:
        print('EMPATE')

    elif escolhacpu == 'TESOURA':
        print('VOCÊ PERDEU!')
        
    elif escolhacpu == 'PEDRA':
        print('VOCÊ GANHOU!')

elif escolha == 3:
    escolha = 'TESOURA'

    print('-=' * 10)
    print(f'VOCÊ ESCOLHEU {escolha} \nEU ESCOLHI {escolhacpu}!')
    print('-=' * 10)

    sleep(1)
    if escolha == escolhacpu:
        print('EMPATE!')

    elif escolhacpu == 'PEDRA':
        print('VOCÊ PERDEU!')

    elif escolhacpu == 'PAPEL':
        print('VOCÊ GANHOU!')
    
    
