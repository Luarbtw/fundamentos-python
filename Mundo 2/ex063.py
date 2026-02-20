print("-" * 20)
print("Sequência de Fibonacci")
print("-" * 20)
quantidade = int(input("Quantos termos você quer mostrar? "))
anterior = 0 #1 #3
atual = 1 #2 #5
print("==" * 20)

while quantidade > 0:
    print(f"{anterior} -> ", end='') 

    novo = anterior + atual 
    anterior = atual 
    atual = novo 

    quantidade -= 1

print("FIM")    
