s = 0
cont = 0
for c in range(0,500):
    if c % 2 == 1 and c % 3 == 0:
        s = s + c # =ou s += c
        cont = cont + 1 #ou cont += 1
print('A soma de todos os {} numeros impares e multiplos de seis\nÉ igual a {}.'.format(cont, s))