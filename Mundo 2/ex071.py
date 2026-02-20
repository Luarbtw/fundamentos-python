print("="*30)
print("SIMULADOR DE SAQUE")
print("="*30)

while True:
    saque = int(input("Quanto você quer sacar? R$"))

    if saque <= 0:
        print("Digite um valor válido!")
        continue

    cedula50 = saque // 50
    resto = saque % 50

    cedula10 = resto // 10
    cedula1 = resto % 10
    break

print(f"Total de {cedula50} cédulas de R$50, {cedula10} cédulas de R$10 e {cedula1} cédulas de R$1")

