frase = input('Digite uma frase: ')

contagem_a = frase.lower().count('a')
contagem_ã = frase.lower().count('ã')

contagem_total = contagem_a + contagem_ã #conta todos as letra 'A'

fraselow = frase.replace(' ', '').lower() #tira os espaços

print(f'A quantidade de vezes que a letra "A" aparece nessa frase é: {contagem_total}')

primeiro_a = fraselow.find('a')
primeiro_ã = fraselow.find('ã')

'''
if primeiro_a <= primeiro_ã: # se 'A' sem acento aparecer primeiro, a posição será mostrada, ou a posição do 'A' com acento tio
    print(f'A primeira posiçao da letra "A" na frase é: {primeiro_a}')
else:
    print(f'A primeira posição da letra "A" na frase é: {primeiro_ã}')

ultimo_a = fraselow.rfind('a')
ultimo_ã = fraselow.rfind('ã')

if ultimo_a >= ultimo_ã: # se 'A' sem acento aparecer por último, a posição será mostrada, ou a posição do 'A' com acento tio
    print(f'A última posição da letra a na frase é: {ultimo_a}')
else:
    print(f'A última posição da letra a na frase é: {ultimo_ã}')

#esqueci dos outros milhares de acentos que 'A' tem

# Outra forma que encontrei de fazer:
contagemDosA = (frase.count('a')) + (frase.count('A'))
print (contagemDosA)'''




