l1 = float(input('Primeira reta: '))
l2 = float(input('Segunda reta: '))
l3 = float(input('Terceira reta: '))
triangle = l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1
if triangle == True:
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')