import os

# Função para limpar o terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Sistema de Controle de Estoque
estoque = []  # Lista principal

while True:
    limpar_tela()
    print("=== CADASTRO DE PRODUTOS ===")
    nome = input("Digite o nome do produto (ou Enter para sair): ")
    if nome == "":
        break

    preco = float(input("Digite o preço do produto: R$ "))
    quantidade = int(input("Digite a quantidade em estoque: "))
    marca = input("Digite a marca do produto: ")

    # Tupla com informações fixas do produto
    info = (nome, marca)

    # Dicionário com todos os dados
    produto = {
        "info": info,
        "preco": preco,
        "quantidade": quantidade
    }

    estoque.append(produto)
    print("\nProduto adicionado com sucesso!")
    input("Pressione Enter para continuar...")

print("\n=== ESTOQUE CADASTRADO ===")

valor_total = 0

for item in estoque:
    nome, marca = item["info"]
    preco = item["preco"]
    quantidade = item["quantidade"]
    total_item = preco * quantidade
    valor_total += total_item

    print(f"Produto: {nome}")
    print(f"Categoria: {marca}")
    print(f"Preço: R$ {preco:.2f}")
    print(f"Quantidade: {quantidade}")
    print(f"Total: R$ {total_item:.2f}")
    print("-" * 30)

print(f"\nValor total do estoque: R$ {valor_total:.2f}")

# --- Busca por categoria ---
while True:
    print("\n=== BUSCA POR MARCA ===")
    busca = input("Digite a marca para buscar (ou Enter para sair): ")
    if busca == "":
        break

    limpar_tela()
    encontrados = [p for p in estoque if p["info"][1].lower() == busca.lower()]

    if encontrados:
        print(f"\nProdutos na marca '{busca}':")
        for p in encontrados:
            nome, marca = p["info"]
            print(f"- {nome} (R$ {p['preco']:.2f}, {p['quantidade']} unidades)")
        print()
    else:
        print("Nenhum produto encontrado nessa marca.\n")

    input("Pressione Enter para continuar...")
    limpar_tela()
