from datetime import date
maiores = 0
menores = 0
atual = date.today().year
for c in range(1, 8):
    n = int(input('Digite o ano de nascimento da {}ª pessoa:' .format(c)))
    idade = atual - n
    if idade >= 18:
        maiores = maiores + 1
    else:
        menores = menores + 1
print('No grupo há {} maior(es) de idade' .format(maiores))
print('e {} menor(es) de idade.' .format(menores))
