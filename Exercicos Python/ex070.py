soma = mil = menor = cont = 0
menorp = ''
print('-' * 20)
print('SUPER LOJAO')
print('-' * 20)
while True:
    produto = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    cont += 1
    soma += preco
    if preco > 1000:
        mil += 1
    if cont == 1 or preco < menor:
        menor = preco
        menorp = produto
    elif preco < menor:
        menor = preco
        menorp = produto
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = input('Deseja continuar? [S/N] ').strip()[0]
    if continuar in 'Nn':
        break
print('O tatal da compra foi de {:.2f}.'.format(soma))
print('Voce comprou um tatal de {} produto(s) por mais de R$1000 reais.'.format(mil))
print('O item mais barato foi {} que custa {}.'.format(menorp, menor))
print('{:-^40}'.format('FIM DO PROGRAMA'))
