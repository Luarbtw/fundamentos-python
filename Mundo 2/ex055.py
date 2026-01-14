pesos = []
for x in range(5):
    peso = float(input(f'Digite o peso da {x + 1}ª pessoa: '))
    pesos.append(peso)
print (f'O menor peso lido foi de: {min(pesos)}Kg')
print (f'O maior peso lido foi de: {max(pesos)}Kg')