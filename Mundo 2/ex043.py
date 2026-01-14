p = float(input('Informe seu peso: '))
a = float(input('Informe sua altura: '))

imc = p / (a ** 2)

print(f'Seu IMC (Índice de Massa Corporal) é: {imc:.1f}')
if imc <= 18.5:
    print('Você está abaixo do seu peso normal.')
elif imc <= 24.9:
    print('Você está no peso ideal (parabéns!)')
elif imc <= 29.9:
    print('Você está levemente acima do peso!')
elif imc <= 34.9:
    print('Voceê está com obesidade grau 1!')
elif imc <= 39.9:
    print('Você está com obesidade graus 2 (severa)!')
else:
    print('Você está com obesidade nível 3 (mórbida)!!!')