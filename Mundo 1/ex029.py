#Sistema de multa
speed = float(input('qual a velocidade atual do carro (em km/h)? '))
multa = float((speed - 80) * 7)
if speed > 80:
    print(f'Você foi multado por ecesso de velocidade em R${multa}')
else:
    print('Dirija com cuidado e tenha um bom dia!')