while True:
    try:
        nm = float(input('insira um numero para conferir sua tabuada: '))
        break
    except:
        print('O valor inserido não é valido, tente novamente.')

while True:
    try:
        tb = int(input('insira até qual tabuada deste numero você deseja: '))
        break
    except:
        print('O valor inserido não é valido, tente novamente.')

for x in range(tb+1):
    print(f'{nm} * {x} = {nm * x}')