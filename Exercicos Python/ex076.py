listagem = ('Lápis', 2.50,
            'Borracha', 2,
            'Caderno', 20.90,
            'Estojo', 25,
            'Transferidor', 4.40,
            'Compasso', 9.99,
            'Mochila', 120,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-'*38)
print(f'{"LOJÃO":^38}')
print('-'*38)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>6.2f}')
