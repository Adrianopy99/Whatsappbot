import pyautogui
import time

time.sleep(5)
pyautogui.moveTo(798,733)
pyautogui.click()
time.sleep(3)
pyautogui.typewrite("Hello World !",interval=0.25)
time.sleep(2)
pyautogui.press("enter")
