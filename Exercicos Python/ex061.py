c = 0
d = 0
print('='*20)
print('10 PRIMEIROS TERMOS')
print('='*20)
n = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Agora digite a rasão da PA: '))
while c <= 10:
    print(' {} '.format(n), end='')
    print('->',end='')
    n += r
    c += 1
print(' FIM')
