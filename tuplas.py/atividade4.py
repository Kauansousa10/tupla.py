texto = input("Palavras separadas por espaço: ")

palavras = texto.split()

unicos = set(palavras)

print("Digitadas:", len(palavras))
print("Únicas:", len(unicos))
print("Palavras:", sorted(unicos))