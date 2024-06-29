print('Você passou por um radar de velocidade onde o limite era 80 Km/H.')
vel= int(input('Digite a quantos Km/H você passou:'))
if vel <=80:
    print('Você passou dentro do limite permitido. Parabens!')
else:
    print('Você foi multado!')
    print('Para cada Km/H a cima da velocidade permitda\nhá um almento de 7 reais na multa.')
    print('Logo,')
    print('A multa a pagar tem o valor de {} reais.'.format((vel-80)*7))
