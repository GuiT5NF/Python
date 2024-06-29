#Progama para saber a categoria de um atleta de natação.
idade=int(input('Digite o ano em que nasceu:'))
cat=2024-idade
if cat<9:
    print('Com {} anos, sua categoria é MIRIM.'.format(cat))
elif cat>9 and cat<14:
    print('Com {} anos, sua categoria é INFANTIL.'.format(cat))
elif cat>=14 and cat<19:
    print('Com {} anos, sua categoria é JUNIOR.'.format(cat))
elif 19 or 20:
    print('Com {} anos, sua categoria é SÊNIOR.'.format(cat))
else:
    print('Com {} anos, sua categoria é MASTER.'.format(cat))
