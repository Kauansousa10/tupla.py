nomes = []

qtd = int(input("Quantos nomes? "))

for i in range(qtd):
    nome = input("Digite um nome: ")
    nomes.append(nome)

unicos = set(nomes)
nomes_ordenados = sorted(unicos)

tupla = (
    nomes_ordenados[0],
    nomes_ordenados[-1]
)

print("Quantidade digitada:", len(nomes))
print("Quantidade única:", len(unicos))
print("Nomes:", nomes_ordenados)
print("Tupla:", tupla)