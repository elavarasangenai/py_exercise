import pyautogui
import time

time.sleep(5)  # Wait for 5 seconds to switch to the desired screen
x, y = pyautogui.position()  # Get the current mouse position       
print(f"Current mouse position: ({x}, {y})")