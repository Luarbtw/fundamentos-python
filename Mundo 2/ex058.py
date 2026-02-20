from random import randint

escolhaPC = randint(0, 10)

print('Vou pensar em um número entre 0 e 10...')
guess = int(input('Adivinhe o número: '))
tentativas = 1

while guess != escolhaPC:
    tentativas += 1
    if guess > escolhaPC:
        print('Menos... Tenta denovo!')
    elif guess < escolhaPC:
        print('Mais... Tenta denovo!')
    guess = int(input('Adivinhe o número: '))
print(f'Você acertou! O número que eu pensei era {escolhaPC} e você disse {guess}, você levou {tentativas} tentativas até acertar!')
