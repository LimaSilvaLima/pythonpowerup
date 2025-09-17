import pyautogui
import time

pyautogui.PAUSE = 1.5

# 1. Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# 2. Entrar no site
time.sleep(3) # Espera o navegador abrir completamente
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3) # Espera a página carregar

# 3. Fazer login
pyautogui.press("tab") # Navega para o campo de email
pyautogui.write("pythonimpressionador@gmail.com")



# importar base de dados
# cadastrar um produto
# repetir cadastramento todos os produtos

# Biblioteca pyautogui : permite controlar mouse e teclado da maquina
# Instalar pip install pyautogui

#Comandos
# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> apertar uma tecla
# pyautogui.write -> escrever um texto
