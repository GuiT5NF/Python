resposta = 's'
soma = cont = num = maior = menor = 0
print('Você recebera a media de todos os valores.')
while resposta in 'Ss':
    num = int(input('Digite um valor: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
media = soma / cont
print('A media dos {} valores é igual a {}.'.format(cont, media))
print('O maior numero digiteto foi {} e o menor foi {}.'.format(maior, menor))
