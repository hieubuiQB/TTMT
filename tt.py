import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)

coors = pyautogui.locateOnScreen('1.png', grayscale=True, confidence=0.9)
coors_center = pyautogui.center(coors)
pyautogui.click(coors_center.x, coors_center.y)

time.sleep(10)
coors = pyautogui.locateOnScreen('2.png', grayscale=True, confidence=0.7)
coors_center = pyautogui.center(coors)
pyautogui.click(coors_center.x + 70, coors_center.y)
pyautogui.typewrite('facebook.com')
pyautogui.press('enter')

time.sleep(10)
coors = pyautogui.locateOnScreen('5.png', grayscale=True, confidence=0.9)
coors_center = pyautogui.center(coors)
pyautogui.click(coors_center.x + 50, coors_center.y)
time.sleep(10)
pyautogui.typewrite('FIFA ONLINE và Garena')
coors = pyautogui.locateOnScreen('11.PNG', grayscale=True, confidence=0.7)
coors_center = pyautogui.center(coors)
pyautogui.click(coors_center.x, coors_center.y)
pyautogui.press('enter')
