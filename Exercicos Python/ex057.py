sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos, Digite novamente: '))
print('O sexo registrado foi {}.'.format(sexo))