import webbrowser, pyautogui
from time import sleep

webbrowser.open('https://www.tiktok.com/pt-BR/')
sleep(5)
pyautogui.click(1756,174, duration=2)
sleep(2)
pyautogui.click(1392,501, duration=2)
sleep(2)
pyautogui.click(1583,406, duration=2)
sleep(2)
pyautogui.click(1448,450, duration=2)
pyautogui.write("email@gmail.com")
sleep(2)
pyautogui.click(1432,519, duration=2)
pyautogui.write("senha")
sleep(2)
pyautogui.click(1469,650, duration=2)
sleep(20)
webbrowser.open('https://www.tiktok.com/@aquela_cenaa')
sleep(5)
pyautogui.click(1274,944, duration=2)
sleep(5)
for video in range(15):
    imagem = pyautogui.locateOnScreen('curtida.png')
    if imagem:
        pyautogui.press('down')
        sleep(5)
    else:
        sleep(5)
        pyautogui.click(1825,467, duration=2)
        sleep(5)
        pyautogui.press('down')  