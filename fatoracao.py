
while True:
    try:
        nm = int(input('Insira um número inteiro para ser fatorado: '))
        break
    except:
        print('O valor inserido não é valido, tente novamente.')
fat = []
fat2 = []
for x in range(nm):
    fat.append(nm-x)
    print(fat)

for x in range(nm):
    x = nm - x - 1
    fat2.append(fat[x])
    print(fat2)

fato = 1

for x in fat2:
    fato *= x
    print(fato)

while True:
    try:
        conf = int(input('Insira o resultado esperado para conferencia: '))
        break
    except:
        print('O valor inserido não é valido, tente novamente.')

if fato == conf:
    print('Fator bate')
else:
    print('Deu erro man')