palavra = input('Inisira uma frase para conferir se ela é um palindromo: ')

pal1 = []
pal2 = []
cont = 0

for x in palavra:
    if x != ' ':
        pal1.append(x)
        cont += 1
for x in range(cont):
    x = cont - x - 1
    pal2.append(pal1[x])
    x = pal1[x].lower
    print(x)

print(pal1)
print(pal2)

if pal1 == pal2:
    print('É um palindromo')
else:
    print('Não é um palindromo')
