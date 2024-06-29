pas= float(input('Qual a distancia que você deseja viajar:'))
if pas <=200:
    print('Viajens de menos de 200Km é cobrado R$0,50 por km.')
    print('Logo, sua viajem custou R${:.2f}.'.format((pas)*0.50))
else:
    print('Viagens de mais de 200Km é cobrado R$0,45 por Km.')
    print('Logo sua viagem custou R${:.2f}.'.format((pas)*0.45))