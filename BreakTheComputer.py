import pyautogui
import time
pyautogui.FAILSAFE = True
time.sleep(1)
x = 0
clicker = 0
def counter():
    global x
    global clicker
    # for i in range(beep):
    while True:
        pyautogui.hotkey("win", "r")
        pyautogui.press("enter")
        # pyautogui.locateOnScreen('C:\Users\Person\Pictures/Click2.png')  # returns (left, top, width, height) of first place it is found
        # pyautogui.click(x=1000, y=50)
        # if clicker == True:
        #     pyautogui.click()
        #     clicker = False
        # else:
        #     clicker = True
        x += 1
        print(f"There are {x} DVD Logos!")
        time.sleep(1
                   )

# counter(100)
counter()
# # C:\Users\Person\Downloads\PythonDVD (2)\dist\label/label.exe

# # ! python3
# import pyautogui, sys
# print('Press Ctrl-C to quit.')
# try:
#     while True:
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#         print(positionStr, end='')
#         print('\b' * len(positionStr), end='', flush=True)
# except KeyboardInterrupt:
#     print('\n')