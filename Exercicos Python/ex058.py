from random import randint
from time import sleep
n = 0
c = 0
print('-='*20)
print('Jogo de adivinhação')
print('-='*20)
comp= randint(0,10)
while c == 0:
    num= int(input('Digite um numero de 0 a 10: '))
    print('PROCESSANDO...')
    sleep(2)
    n += 1
    if num == comp:
        c += 1
    else:
        if num < comp:
            print('Errou! É um numero \033[4;31mmaior!\033[m')
        elif num > comp:
            print('Errou! É um numero \033[4;34mmenor!\033[m')
print('O numero escolhido por mim foi {}. Você acertou!'.format(comp))
print('Você precisou de {} tentaivas'.format(n))
