import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write("hora")
pyautogui.press('enter')

while not pyautogui.locateOnScreen('button-to-click.jpeg', confidence=0.5):
    time.sleep(1)

x, y, largura, altura = pyautogui.locateOnScreen('button-to-click.jpeg',confidence=0.5)
pyautogui.click(x + largura/2, y + altura/2)

pyautogui.hotkey('alt', 'f4')