d = float(input('Qual a distância da viagem? '))
price1 = d * 0.50
price2 = d * 0.45
if d <= 200:
    print(f'O preço de uma viagem de {d}Km será de R${price1:.2f}')
else:
    print(f'O preço de uma viagem de {d}Km será de R${price2:.2f}')