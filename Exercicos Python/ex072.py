cont = ('zero', 'um', 'dois', 'tres', 'quatro', ' cinco', 'seis',
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze',
        'dezeseis', 'dezessete', 'desoito', 'desenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um numero de 0 a 20: '))
        if 0 < num < 20:
            break
        else:
            print('Tente novamente.', end='')
    print(f'O numero digitedo foi {cont[num]}.')
    resp = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if resp == 'N':
        break
print('Adeus.')