import pyautogui
import time

# Before starting make sure you have installed 'pyautogui' library
# Just to make sure write 'pip install pyautogui' on terminal/command line 
# This way it will install library if it is not already installed

# 1- uncomment line 35
# 2- open terminal and run the program using 'py clickbot.py' command 
# 3- program will open a mouse info program 
# 4- open your game on emulator and find the mouse positions for the first click(a, b)
# 5- find the mouse click for (c, d)
# tip: to find the coordinates easily while the  python program was running go 
#      to the emulator click on the python program and then while your mouse 
#      was in position press F6 to create log. Do it for the two coordinates
# 6- uncomment line 33, comment line 35
# 7- When you learn both coordinates change (a, b, c, d) accordingly on line 
# 8- and change the times on click function with the number of fireworks you have
# 9- run python program again and you will have 5 seconds to open emulator app
# 10- don't interfere with pc and let the bot do its job 


def click(a, b, c, d, times):
    time.sleep(5)
    while times > 0:
        times -= 1
        pyautogui.click(a, b)
        time.sleep(1)
        pyautogui.click(c, d)
        time.sleep(5)


# click(1653,858, 1176,841, 36)

# pyautogui.mouseInfo()