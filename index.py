import pyautogui
import time

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write("hora")
pyautogui.press('enter')

pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')

pyautogui.hotkey('enter')

time.sleep(1)

pyautogui.hotkey('alt', 'f4')