import time
import keyboard
import pyautogui
import win32api
import win32con
time.sleep(5)

#Kodlar ekranda im.png yi gördüğünde imleci üstüne getirip tıklaması içindir.
#Otomasyonlarınız için faydalı olabilir.

c = int(input("Çözünürlüğünüzün genişliğini belirtiniz (Örn:1600) : "))

v = int(input("Çözünürlüğünüzün yüksekliğini belirtiniz (Örn:900) : "))

b = input("Başlatmak için enter ")

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(0.1)


while not keyboard.is_pressed('q'):
    start = pyautogui.locateCenterOnScreen('im.png', region=(0, 0, c, v), grayscale=True, confidence=0.70)
    if start is not None:
        pyautogui.moveTo(start)
        click()

#Not : CS:GO AimBot yapmayın ban yersiniz. :)