ano= int(input('Digite qualquer ano ara saber se ele é bissexto ou não:'))
res= ano % 4
if res == 0:
    print('O ano de {} é bissexto!'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))
