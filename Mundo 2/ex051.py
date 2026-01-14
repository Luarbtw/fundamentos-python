p1 = int(input('Qual o primeiro termo da PA? '))
r = int(input('Qual a razão da PA? '))

contador = 0

for c in range(10):
    valor = p1 + (contador * r)
    print(valor)
    contador += 1