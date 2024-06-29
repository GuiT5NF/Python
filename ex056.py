somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulheres20 = 0
for p in range (1,5):
    print('------ {}ª PESSOA------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulheres20 += 1
mediaidade = somaidade / 4
print('A media da idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('No grupo há {} mulher(es) com menos de 20 anos.'.format(totmulheres20))
