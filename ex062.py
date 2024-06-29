print('GERDOR DE PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo),end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce deseja a mais: '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
