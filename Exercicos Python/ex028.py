from random import randint
from time import sleep
print('-='*20)
print('Jogo de adivinhação')
print('-='*20)
comp= randint(0,5)
num= int(input('Digite um numero de 0 a 5:'))
print('PROCESSANDO...')
sleep(3)
if num == comp:
    print('O numero escolhido por mim foi {}. Você acertou!'.format(comp))
else:
    print('O numero escolhido por mim foi {}. Você errou!'.format(comp))
