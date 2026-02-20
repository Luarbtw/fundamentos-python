n = contador = acumulador = 0

while n != 999:
    acumulador += n
    n = int(input("Digite um numero [999 para parar]: "))
    if n != 999:
        contador += 1

print(f"Você digitou {contador} valores e o total da soma desses valores é: {acumulador}")
    