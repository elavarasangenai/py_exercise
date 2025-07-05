import pyautogui
import time
import webbrowser

# Set delay between PyAutoGUI calls
pyautogui.PAUSE = 1

time.sleep(5)

# Step 1: Open the browser and go to WhatsApp Web
webbrowser.open("https://web.whatsapp.com")
time.sleep(10)  # Wait for WhatsApp Web to load & user to scan QR

# Step 2: Click on the search bar
# You need to manually get the coordinates of the search bar
# Move your mouse to search bar and run pyautogui.position() in console to get coordinates
pyautogui.click(x=476, y=209)
time.sleep(2)

# Step 3: Type the contact name
contact_name = "elavarasan"
pyautogui.write(contact_name)
time.sleep(2)

pyautogui.click(x=366, y=513)
pyautogui.press('enter')
time.sleep(2)

pyautogui.click(x=938, y=970)

# Step 5: Type the message
message = "Hello from PyAutoGUI!"
pyautogui.write(message)

time.sleep(1)

# # Step 6: Press Enter to send the message
pyautogui.press('enter')

print("Message sent!")

