matriz = [[],[],[]]

for linha in range(3):
    for coluna in range(3):
        x = int(input(f"Digite um valor pra posição [{linha}, {coluna}]: "))
        matriz[linha].append(x)

for linha in matriz:
    for num in linha:
        print(f"[{num}]", end=' ')
    print()




    
    
    

