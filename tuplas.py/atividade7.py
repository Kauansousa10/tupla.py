produtos = [
    {"nome": "Mouse", "preco": 50, "categoria": "Informática"},
    {"nome": "Teclado", "preco": 80, "categoria": "Informática"},
    {"nome": "Caderno", "preco": 20, "categoria": "Papelaria"},
    {"nome": "Caneta", "preco": 5, "categoria": "Papelaria"}
]

valor = float(input("Mostrar produtos acima de qual preço? "))

filtrados = [p for p in produtos if p["preco"] > valor]

ordenados = sorted(produtos, key=lambda p: p["preco"])

categorias = {p["categoria"] for p in produtos}

precos = [p["preco"] for p in produtos]

estatisticas = (
    min(precos),
    max(precos),
    sum(precos) / len(precos)
)

print("\nProdutos filtrados:")
for produto in filtrados:
    print(produto["nome"], "-", produto["preco"])

print("\nProdutos ordenados:")
for produto in ordenados:
    print(produto["nome"], "-", produto["preco"])

print("\nCategorias:", categorias)

print("\nEstatísticas:")
print("Menor preço:", estatisticas[0])
print("Maior preço:", estatisticas[1])
print("Média:", estatisticas[2])