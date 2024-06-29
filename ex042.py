#copia do ex035, mas agr mostrar se é equilatero, isosceles ou escaleno
print('-='*20)
print('Analisador de trinagulos')
print('-='*20)
l1= float(input('Digite um lado do triangulo:'))
l2= float(input('Digite outro lado:'))
l3= float(input('Digite o ultimo lado:'))
if l1+l2>l3 and l2+l3>l1 and l3+l1>l2 and l1==l2==l3:
    print('Essas retas formam um trinagulo equilatero.')
elif l1+l2>l3 and l2+l3>l1 and l3+l1>l2 and (l1==l2!=l3 or l2==l3!=l1 or l3==l1!=l2):
    print('Essas retas formam um triangulo isosceles.')
elif l1+l2>l3 and l2+l3>l1 and l3+l1>l2 and (l1!=l2!=l3):
    print('Essas retas formam um triangulo escaleno.')
else:
    print('Suas medidas sao impossiveis de fazer um trianguilo.')
