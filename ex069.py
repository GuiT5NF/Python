dezoito = homens = vinte = 0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    while idade < 0:
        idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ').strip().upper()[0])
    while sexo not in 'FfMm':
        sexo = str(input('Sexo [M/F]: ').strip().upper()[0])
    print('-'*20)
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if idade > 18:
        dezoito += 1
    if sexo in 'Mm':
        homens += 1
    if idade < 20 and sexo in 'Ff':
        vinte += 1
    if continuar in 'Nn':
        break
print('Numero de pessoas com mais de 18 anos: {}'.format(dezoito))
print('Numero de homens cadastrados: {}'.format(homens))
print('Numero de mulheres com menos de 20 anos: {}'.format(vinte))

