print('-='*20)
print('Analisador de trinagulos')
print('-='*20)
l1= float(input('Digite um lado do triangulo:'))
l2= float(input('Digite outro lado:'))
l3= float(input('Digite o ultimo lado:'))
if l1+l2>l3 and l2+l3>l1 and l3+l1>l2:
    print('Essas retas podem formar um trinagulo.')
else:
    print('Suas medidas sao impossiveis de fazer um trianguilo.')
