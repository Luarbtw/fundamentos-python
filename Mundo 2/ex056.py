contador = 0
somaidade = 0
mediaidade = 0
maioridade = 0
mulheres20 = 0

for x in range(4):
    print(f'{contador + 1}a Pessoa')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    contador += 1
    somaidade += idade
    if x == 1 and sexo in 'Mm':
        maioridade = idade
        nomehomem = nome
    if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomehomem = nome
    if sexo in 'Ff' and idade < 20:
        mulheres20 += 1

mediaidade = somaidade / 4

print(f'A média da idade do grupo é: {mediaidade}.')
print(f'O homem mais velho se chama {nomehomem}.')
print(f'{mulheres20} mulheres possuem menos de 20 anos de idade.')