frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('A o inverso de {} é {}.'.format(frase, inverso))
if inverso == frase:
    print('Temos um PALINDROMO!')
else:
    print('Não temos um PALINDROMO!')

