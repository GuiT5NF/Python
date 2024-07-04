import openpyxl
from urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui

webbrowser.open('https://web.whatsapp.com')
sleep(10)

#ler planilha e guardar informacoes sobre nome, telefone e data de vencimento
workbook = openpyxl.load_workbook('Clientes.xlsx')
pagina_clientes = workbook['Sheet1']

for linha in pagina_clientes.iter_rows(min_row=2):
    #nome, telefone, vencimento
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value

    mensagem = f'Ola {nome}, seu boleto vence no dia {vencimento.strftime('%d/%m/%Y')}. Mande no seguinte pix:... '

    # criar links personalizados do whatsapp e enviar para cada cliente
    # https://web.whatsapp.com/send?phone={}&text={quote()}
    try:
        link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
        webbrowser.open(link_mensagem_whatsapp)
        sleep(10)
        seta = pyautogui.locateCenterOnScreen('seta.png')
        sleep(5)
        pyautogui.click(seta[0],seta[1])
        sleep(5)
        pyautogui.hotkey('ctrl','w')
        sleep(5)
    except:
        print(f'Não foi possivel mandar mensagem para {nome}')
        with open('Erros.csv','a',newline='',encoding='utf-8') as arquivo:
            arquivo.write(f'{nome},{telefone}')
#com base nos dados da planilhax