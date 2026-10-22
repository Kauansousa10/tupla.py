texto = input("Números separados por espaço: ")

numeros = [int(x) for x in texto.split()]

numeros.sort()

print("Crescente:", numeros)
print("Decrescente:", sorted(numeros, reverse=True))