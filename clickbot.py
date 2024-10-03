import pyautogui
import time

def click(x1, y1, x2, y2, times):
    time.sleep(5)
    while times > 0:
        times -= 1
        pyautogui.click(x1, y1)
        time.sleep(1)
        pyautogui.click(x2, y2)
        time.sleep(5)

print("\n       ---User-Instructions---\n")
print("1- Make sure your screen resolution is 1920x1080")
print("2- If you have different screen resolution change it to 1920*1080")
print("3- After entering inputs you will have 5 seconds to switch to your emulator ")
print("4- Make sure to open the emulator at full screen after entering inputs")
print("5- Enter the needed inputs and it will start working automatically ")
print("\n       ---End of instructions---\n")
whichOne = int(input("For big firework enter 1 for middle firework enter 2  for small firework enter 3: "))
times = int(input("Enter how many fireworks you have: "))

if(whichOne == 3):
    click(1563,900, 971,900, times)
elif(whichOne == 2):
    click(1563,900, 1168,900, times)
elif(whichOne == 1):
    click(1563,900, 1355,900, times)

# pyautogui.mouseInfo()

# The code at line 30 opens a coordinate finder: 
# if your screen resolution is not 1920*1080 and don't want to  change it 
# comment all the other code and uncomment line 30 this way 
# you can find the right coordinates for your screen resolution 
# after finding the right resolution change x1, y1, x2, y2 accordingly