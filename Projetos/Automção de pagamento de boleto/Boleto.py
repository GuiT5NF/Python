import pyautogui
import time
pyautogui.PAUSE = 0.5
pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')
time.sleep(2)
pyautogui.write('https://portal.univap.br/portal/')
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(x=1091, y=544) # clicando no aluno
time.sleep(1)
pyautogui.click(x=941, y=683) # clicando em entrar
pyautogui.click(x=972, y=683) # Por segurança evitar o anuncio
pyautogui.click(x=1189, y=201) # clicando em extrato
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=967, y=437) # baixando o boleto
time.sleep(1)
pyautogui.hotkey('ctrl','t')
pyautogui.write('https://web.whatsapp.com')
pyautogui.press('enter')
time.sleep(10)
pyautogui.click(x=291, y=218) # barra de pesquisa do whatsapp
pyautogui.write('Contato whatsapp')
pyautogui.press('enter')
pyautogui.click(x=796, y=960) # mais
pyautogui.click(x=861, y=634) # documentos
pyautogui.click(x=755, y=680) # clicando no ultimo pdf
time.sleep(1)
pyautogui.press('enter')