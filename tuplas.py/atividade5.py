texto = input("Notas separadas por espaço: ")

notas = [float(x) for x in texto.split()]

estatisticas = (
    min(notas),
    max(notas),
    sum(notas) / len(notas)
)

print("Mínimo:", estatisticas[0])
print("Máximo:", estatisticas[1])
print("Média:", estatisticas[2])