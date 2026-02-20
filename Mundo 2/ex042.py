l1 = float(input('Primeira reta: '))
l2 = float(input('Segunda reta: '))
l3 = float(input('Terceira reta: '))
triangle = l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1
if triangle == True:
    if l1 == l2 or l1 == l3 or l2 == l3:
        print('É possível formar um triângulo ISÓSCELES')
    elif l1 == l2 == l3:
        print('É possível formar um triângulo EQUILÁTERO')
    elif l1 != l2 != l3:
        print('É possível formar um triângulo ESCALENO')
else:
    print('Não é possível formar um triângulo.')