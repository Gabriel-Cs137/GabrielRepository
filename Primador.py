nm = 0
primo = []
primo2 = [2,3,5,7]
primer = False
def pedir_numero():
    global nm
    while True:
        try:
            nm = int(input('Insira um número: '))
            break
        except:
            print('Valor inválido, tente novamente.')
    print('=====================================================')

def calc(type,nm):
    global primo, primer, primo2
    
    if type == 1:
        if nm <= 1:
            primer = False
        elif nm == 2 or nm == 3 or nm == 5 or nm == 7:
            primer = True
        else:

            for x in primo2:
                if nm % x != 0:
                    primer = True
                else:
                    primer = False
                    break
            if primer == True:
                primo2.append(nm)
                primo.append(nm)

    else:
        pass
while True:
        verif = input('O que gostaria de fazer?\n[1- Verificar se um número é primo]\n[2-Verificar quais numeros dentro de um range]\n[3- Fechar o sistema]\n[]:')
        if verif == '1':
            pedir_numero()
            calc(1,nm)
            if primer == True:
                print('é um número primo')
            else:
                print('Não é um número primo')
            print('=====================================================')
        elif verif == '2':
            pedir_numero()
            primo = []
            for x in range(nm):
                calc(1,x)
            print(f'primos encontrados: {primo}')
            print('=====================================================')
        elif verif == '3':
            break
        else:
            print('Opção inválida, tente novamente.')
