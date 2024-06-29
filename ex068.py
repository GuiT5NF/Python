import random
cont = 0
print('-='*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*20)
while True:
    n = int(input('Diga seu valor: '))
    escolha = ' '
    while escolha not in 'PpIi':
        escolha = input('Par ou impar? [P/I]: ').strip().lower()[0]
    comp = random.randint(0,10)
    soma = comp + n
    print('Voce escolheu {} e eu {}, somando {}.'.format(n, comp, soma))
    if escolha in 'Pp':
        if soma % 2 == 0:
            print('Voce ganhou, vamos continuar.')
            print('-'*10)
            cont += 1
        else:
            print('Voce perdeu.')
            break
    elif escolha in 'Ii':
        if soma % 2 == 1:
            print('Voce ganhou, vamos continuar.')
            print('-'*10)
            cont += 1
        else:
            print('Voce perdeu.')
            break
print('O jogo acabou e voce ganhou um total de {} partida(s) consecutiva(s)!'.format(cont))
