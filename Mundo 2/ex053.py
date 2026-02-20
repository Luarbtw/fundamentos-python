frase = str(input('Escreva palavra ou frase: ')).strip().upper().replace(' ', '')
if frase == frase[::-1]:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo.')
print('A frase lida normalmente seria:',(frase))
print('A frase lida de trás pra frente seria:',(frase[::-1]))
