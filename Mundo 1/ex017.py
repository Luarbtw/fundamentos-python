from math import hypot as hpt
cto = float(input('Digite a medida do cateto oposto: '))
cta = float(input('Digite a medida do cateto adjacente: '))
hipot = hpt(cta, cto)
print (f'A hipotenusa deste triângulo é: {hipot:.2f}')
