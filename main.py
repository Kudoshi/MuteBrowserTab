import pyautogui
import keyboard
from playsound import playsound
from pathlib import Path
import time

'''
Program looks for the current tab open based on the currentTab and currentTab_unfocused image 
given. (Screenshot of the browser's tab)

It finds the location of the image given and then moves there. Right click and move slightly down to click the mute button.
You might have to screenshot the current tab's image as shown in the picture given and then adjust the confidence level
of the pyautogui.locateCenterOnScreen()

Hotkeys:
Ctrl+M = Mute/unmute current tab
Ctrl+Q = Quit program

It plays sound to notify whether it could find a current tab.
'''


soundFile = None

#Set file path of sfx
originalPath = Path(__file__).parent.resolve()
failSfx = originalPath / "Audio" / "Fail.mp3"
accept1Sfx = originalPath / "Audio"/ "Accept1.mp3"
accept2Sfx = originalPath / "Audio"/ "Accept2.mp3"

print("_"*70 ,"\n[START] Program started")
while True:

    #If hotkey is pressed
    if keyboard.is_pressed("ctrl") and keyboard.is_pressed("m"):
        originalPos = pyautogui.position()
        tabLocation1 = pyautogui.locateCenterOnScreen("currentTab.png", confidence=0.94)
        tabLocation2 = pyautogui.locateCenterOnScreen("currentTab_unfocused.png", confidence=0.94)

        # Get location of current tab
        if tabLocation1 != None:
            selectedLocation = tabLocation1
        elif tabLocation2 != None:
            selectedLocation = tabLocation2
        else:
            selectedLocation = None

        # Move mouse
        if selectedLocation != None:
            pyautogui.moveTo(selectedLocation[0] - 8, selectedLocation[1] - 13)
            pyautogui.click(button="right")
            pyautogui.move(50, 240)
            pyautogui.click()
            pyautogui.moveTo(originalPos)

            # Set alternating sound fx
            if soundFile != accept2Sfx:
                soundFile = accept2Sfx
            else:
                soundFile = accept1Sfx

            #Play success sound
            playsound(str(soundFile))

        else:
            #Play fail sound
            playsound(str(failSfx))

    if keyboard.is_pressed("ctrl") and keyboard.is_pressed("q"):
        quit()
    
    time.sleep(0.01)
