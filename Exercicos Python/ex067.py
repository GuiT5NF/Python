cont = 1
while True:
    n = int(input('Digite um valor para saber sua tabuada:'))
    print('-'*20)
    if n < 0:
        break
    while cont <= 10:
        print('{} x {} = {}'. format(n, cont, n*cont))
        cont += 1
    cont = 0
    print('-'*20)
print('Programa de tabuadas encerrado.'.upper())

