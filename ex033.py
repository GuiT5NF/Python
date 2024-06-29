a= float(input('Digite um valor:'))
b= float(input('Digite outro:'))
c= float(input('Digite o Ultimo:'))
menor= a
#Verificando quem é o menor
if b < a and b < c:
    menor=b
if c < a and c < b:
    menor= c
#Verificando quem é o menor
maior= a
if b > a and b > c:
    maior= b
if c > b and c > a:
    maior= c
print('O menor valor digitado foi: {}'.format(menor))
print('O maior valor digitado foi: {}'.format(maior))
