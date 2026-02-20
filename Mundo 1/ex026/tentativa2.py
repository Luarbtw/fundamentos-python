frase = input('Digite uma frase: ')

a = frase.lower().count('a')
ã = frase.lower().count('ã')
â = frase.lower().count('â')
á = frase.lower().count('á')
à = frase.lower().count('à')

contagem = a + ã + â + á + à #conta todos as letra 'A'

fraselow = frase.replace(' ', '').lower() #tira os espaços

index_a = fraselow.find('a')
index_ã = fraselow.find('ã')
index_â = fraselow.find('â')
index_á = fraselow.find('á')
index_à = fraselow.find('à')

lista_index = [index_a, index_ã, index_â, index_á, index_à]

lista_cresc = sorted(lista_index)

menor_index = min(lista_index)

maior_index = max(lista_index)

print(f'A quantidade de vezes que a letra "A" aparece nessa frase é: {contagem}')

print(f'A primeira vez que a letra "A" aparece na frase é na posição: ') # não consegui

print(f'A última vez que a letra "A" aparece na frase é a posição: {maior_index}')
