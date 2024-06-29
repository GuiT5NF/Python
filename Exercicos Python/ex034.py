sal= float(input('Digite o salario do funcionaro: R$'))
if sal >1250:
    print('Para funcionarios com salario superior a R$1250')
    print('o aumento é de 10%.')
    print('Portanto seu novo salrio sera de R${:.2f}'.format(sal*1.1))
else:
    print('Para salarios inferiores ou iguais a R$1250')
    print('o almento é de 15%.')
    print('Portanto seu novo salario sera de R${:.2f}'.format(sal*1.15))
