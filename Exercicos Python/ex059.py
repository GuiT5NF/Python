c = 0
n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro:'))
while c == 0:
    print('OQUE DESEJA FAZER COM ELES:')
    opção = int(input('[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos numeros \n[5] Sair do programa\n').strip())
    if opção == 1:
        soma = n1 + n2
        print('A soma deles é igual a {}.'.format(soma))
    elif opção == 2:
        mult = n1 * n2
        print('A multiplicação entre eles é igual a {}.'.format(mult))
    elif opção == 3:
        if n1 > n2:
            print('O numero {}  é o maior.'.format(n1))
        elif n2 > n1:
            print('O numero {}  é o maior.'.format(n2))
        else:
            print('Os numeros são iguais.')
    elif opção == 4:
        n1 = int(input('Digite um valor:'))
        n2 = int(input('Digite outro:'))
    elif opção == 5:
        print('Finalizando programa.')
        c += 1
    else:
        print('Por favor digite apenas os valores pedidos.')
