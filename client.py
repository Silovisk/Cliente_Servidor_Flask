import requests
import pyautogui
import ctypes

# Captura de tela
screenshot = pyautogui.screenshot()
screenshot.save('screenshot.png')


ip = '000.0.0.0'

# Envia a captura de tela para o servidor doméstico
files = {'screenshot': open('screenshot.png', 'rb')}
response = requests.post(f'http://{ip}:8000/screenshot', files=files)

# Exibe o alerta
ctypes.windll.user32.MessageBoxW(0, f"{response.text}", "Alerta", 0x40)

