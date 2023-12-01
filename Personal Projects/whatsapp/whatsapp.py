import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
import emoji
import random
import time

def send_whatsapp_message(phoneNumber, msg, hour, minute):
    try:
        pywhatkit.sendwhatmsg(phoneNumber, msg, hour, minute)
        time.sleep(15)
        pyautogui.click()
        time.sleep(1)
        Controller().press(Key.enter)
        Controller().release(Key.enter)
        time.sleep(1)
        print("Message sent!")
    except Exception as e:
        print(str(e))

theMessage = random.choice(['Good Day, Your account is now overdue.',
             'Your account is now overdue, please pay urgently.',
             emoji.emojize('Your account is overdue, please pay to avoid suspension.'),
             emoji.emojize('Your account is overdue and may be blocked, please make payment.')
             ])

phoneNumber = input('What number would you like to text? number must include the country calling code  ')
numberOfMessages = int(input('How many times would you like to send a message?  '))
startingHour = int(input('This script sends messages randomly between 2 hours.\nWhat hour would you like to start?  '))
endingHour = int(input('What hour whould you like to stop?  '))

while numberOfMessages != 0:
    hour = random.randrange(startingHour, endingHour)
    minute = random.randrange(0, 60)
    numberOfMessages -= 1
    send_whatsapp_message(phoneNumber, theMessage, hour, minute)