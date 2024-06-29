cont = soma = 0
print('Digite numeros para ir somando.')
print('Digite 999 para encerrar o programa.')
num = int(input('Digite o Valor: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite o Valor: '))
print('A soma de todos os {} numeros digitados foi {}'.format(cont, soma))
