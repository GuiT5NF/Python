times = ('botafogo', 'palmeiras', 'flamengo', 'bahia', 'sao paulo', 'cruzeiro',
         'fortaleza', 'atletico-pr', 'bragantino', 'atletico-mg', 'vasco', 'internacional',
         'juventude', 'criciuma', 'ec vitoria', 'cuiaba', 'corinthians',
         'gremio', 'atletico-go', 'fluminense')
print('-=' * 20)
print('INFOS BRASILEIRÃO')
print('-=' * 20)
print('Os 5 primeiros colocados são:', times[0:5])
print('Os quatro ultmos da tabela são : ', times[-4:])
print('A ordem alfabrtica dos times é: ', sorted(times))
print(f'O fluminense esta na {times.index('fluminense')+1}° posição.')
