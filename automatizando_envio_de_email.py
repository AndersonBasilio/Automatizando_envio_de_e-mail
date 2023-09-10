import pyautogui
from time import sleep
from datetime import datetime

hora = datetime.now()
hora_atual = hora.hour

nome = input('Informe seu nome: ')
endereco_email = input('Digite o endereço do email: ') 
assunto = input('Digite o assunto: ')   
nome_arquivo = input('Informe o nome do arquivo: ')
if hora_atual >= 1 and hora_atual < 12:
    mensagem = (f'Bom Dia! Espero que esteja bem.\nSou {nome}, estudante de Analise e Desenvolvimento de Sistemas e gostaria de uma oportunidade.')

elif hora_atual >= 12 and hora_atual < 18:
    mensagem = (f'Boa Tarde! Espero que esteja bem.\nSou {nome}, estudante de Analise e Desenvolvimento de Sistemas e gostaria de uma oportunidade.')

else:
    mensagem = (f'Boa Noite Espero que esteja bem.\nSou {nome}, estudante de Analise e Desenvolvimento de Sistemas e gostaria de uma oportunidade.')
 

pyautogui.PAUSE = 3
# Entrar no meu iniciar
pyautogui.press('win')

# Na area de pesquisa digito Google Chrome
pyautogui.write('Google Chrome')
pyautogui.press('enter')

# Entrar no gmail
pyautogui.write('gmail.com')
pyautogui.press('enter')

# Clicar em escrever email
pyautogui.click(x=100, y=203)

# Preencher os campo do e-mail
pyautogui.write(endereco_email)
pyautogui.press('tab')
sleep(2)
pyautogui.press('tab')

#Preencher o campo de Assunto
pyautogui.write(assunto)
sleep(1)
pyautogui.press('tab')
sleep(2)

# Mensagem 
pyautogui.write(mensagem)
sleep(2)
pyautogui.click(x=1426, y=1000)
sleep(2)

pyautogui.click(x=89, y=246)
sleep(2)

pyautogui.click(x=198, y=478)
sleep(2)

pyautogui.write(nome_arquivo)
sleep(2)

pyautogui.press('enter')
sleep(2)

pyautogui.click(x=1311, y=1010)

print('E-mail enviado com Sucesso!!!')