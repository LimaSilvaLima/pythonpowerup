import pyautogui

pyautogui.PAUSE = 0.5
#abrir navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#Digitar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#esperar 3 segundos
pyautogui.sleep(3)

#fazer  login
#pyautogui.position (posiçao na tela)
pyautogui.click(x=649, y=477)
pyautogui.write("pythonimpressionador@gmail.com")



# https://dlp.hashtagtreinamentos.com/python/intensivao/login
# fazer login
# importar base de dados
# cadastrar um produto
# repetir cadastramento todos os produtos

# Biblioteca pyautogui : permite controlar mouse e teclado da maquina
# Instalar pip install pyautogui

#Comandos
# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> apertar uma tecla
# pyautogui.write -> escrever um texto



