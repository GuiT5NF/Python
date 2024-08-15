num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite o ultimo numero numero: ')))
print(f'Você digitou os valores {num}')
print(f'O numero 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O numero 3 aparceu na poaição {num.index(3) + 1} .')
else:
    print(f'O numero 3 não foi digitado.')
print(f'Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
