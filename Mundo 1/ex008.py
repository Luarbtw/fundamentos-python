m = float(input('Quantos metros? '))
cm = m * 100
dm = m * 10
mm = m * 1000
km = m/1000
dam = m/10
hm = m/100
print (f'A conversão para decimetros é {dm}dm, para centímetros é {cm}cm, para milímetros é {mm}mm;')
print (f'Para decâmetros é {dam:.3f}dam, para hectômetros é {hm:.4f}, e para quilometros é {km:.4f}km.')
