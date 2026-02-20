from math import sin, tan, cos, radians as rad
ang = int(input('Digite um ângulo: '))
angrad = rad(ang)
sinAng = sin(angrad)
tanAng = tan(angrad)
cosAng = cos(angrad)
print (f'O seno deste ângulo é {sinAng:.3f}, o cosseno é {cosAng:.3f} e a tangente é {tanAng:.3f}.')
