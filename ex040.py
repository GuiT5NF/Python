n1=float(input('Digite a primeira nota:'))
n2=float(input('Digite a segunda nota'))
media=(n1+n2)/2
print('Sua media é {}!'.format(media))
if media<5:
    print('Você esta reprovado!')
elif media>=5 and media<=6.9:
    print('Foi quase! Esta de recuperação.')
else:
    print('Parabens! Você foi aprovado.')