'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''
frase = str(input('Escreva uma frase: '))
#tirando espaços e colocando tudo em minusculo
frase_prep = frase.lower().strip()
#transformando todo A com acento em 'A' e tirando os espaços entre as palavras
A = frase_prep.replace('á' , 'a').replace('â' , 'a').replace('ã' , 'a').replace('à' , 'a').replace(' ', '')
#contagem de todos os A corretamente
contagem = A.count('a')

primeiro = A.find('a')
ultimo = A.rfind('a')

print(f'A quantidade de letras "A" nessa frase é: {contagem}')
print(f'O primeiro "A" está na posição: {primeiro + 1}')
print(f'O ultimo a está na posição: {ultimo + 1}')




