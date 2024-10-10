notas = []

media = 0

for x in range(4):
    notas.append(float(input('Adiciona uma nota:')))

for x in range(4):
    media += notas[x]

media /= 4

print(media)