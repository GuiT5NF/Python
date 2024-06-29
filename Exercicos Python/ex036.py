casa=float(input('Qual o valor da casa que deseja comprar: R$'))
sal=float(input('Digite seu salario: R$'))
ano=int(input('Em quantos anos deseja pagar essa casa:'))
pres=casa/(ano*12)
print('Voce ira pagar {} por mes.'.format(pres))
if pres:
    print('Você pode pagar pela sua casa, parabens!')
else:
    print('O valor dessa casa é muito alta para seu salario atual.')