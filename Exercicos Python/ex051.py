print('='*20)
print('10 PRIMEIROS TERMOS')
print('='*20)
n = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Agora digite a rasão da PA: '))
d = n + (10 - 1) * r
for c in range(n,d + r,r):
    print(c,end=' -> ')
print('Acabou.')