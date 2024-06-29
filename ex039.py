ano=int(input('Digite o ano qe você nasceu:'))
idade=2024-ano
tempo=idade
if idade<18:
    print('Ainda nao é necessario se alistar')
    print()
elif idade==18:
    print('Ja esta na hora de se alistar')
else:
    print('Ja passou da hora de se alistar!')