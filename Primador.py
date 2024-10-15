
def primos(nm):
            global primo
            
            if nm == 2:
                print('É Primo')
                primo.append(nm)

            
            elif nm <= 1:
                print('Não é primo')
                

            elif nm == 3:
                print('É primo')
                primo.append(nm)


            elif nm == 5:
                print('É primo')
                primo.append(nm)


            elif nm == 7:
                print('É primo')
                primo.append(nm)


            elif nm == 11:
                print('É primo')
                primo.append(nm)


            else: 
                if nm % 2 != 0 and nm % 3 != 0 and nm % 5 != 0 and nm % 7 != 0 and nm % 11 != 0 :
                    primador = True
                    if primos != []:
                        for x in primo:
                            if nm % x != 0:
                                pass
                            elif nm % x == 0:
                                primador = False
                                print('Não é primo.')
                                break
                    if primador == True:
                        print('É primo.')
                        primo.append(nm)
                        print(f'primos encontrados: {primo}')
                    else:
                        print('Não é primo')
                else:
                    print('Não é primo')

while True:
    verif = input('Deseja testar um range de números ou um número especifico? \n[N = Fechar|A = Número especifico|R = Range]: ')
    if verif == 'N':
        break
    elif verif == 'A':
        while True:
            try:
                nm =int(input('Insira o número que deseja verficar: '))
                break
            except:
                print('Insira um valor válido')
            
        primos(nm)

    else:
        while True:
            try:
                nm =int(input('Insira a quantidade de número que deseja verficar: '))
                break
            except:
                print('Insira um valor válido')

        primo = []
        
        for y in range(nm):
            primos(y)
