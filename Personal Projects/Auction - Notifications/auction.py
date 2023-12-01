"""
App to notify when the reqiured lots on Auction Nation South Africa are close to being auctioned.
"""
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import sys
from gtts import gTTS
import pygame
from gtts.tokenizer import pre_processors
import gtts.tokenizer.symbols
from twilio.rest import Client


def main():
    #Global varibles
    global link
    global twilioCli
    global myTwilioNumber
    global myCellPhone

    #Enter link for the auction e.g 'https://www.auctionnation.co.za/Auctions/Live/397716'.
    link = 'https://www.auctionnation.co.za/Auctions/Live/397716'
    #Enter list of required lot numbers.
    lots = [162, 193]
    
    #Twilio account details - for receiving sms
    #accountSID = 'your accountSID details goes here'
    #authToken  = 'your authToken details goes here'
    #twilioCli = Client(accountSID, authToken)
    #myTwilioNumber = 'your Twilio Number goes here'
    #myCellPhone = 'your Cell Phone goes here'

    while True:
        time_stamp = time.time()
        running_lots = []
        current_lot = get_currentlot()
        current_time = datetime.now().strftime('%H:%M:%S')
        print(f'{current_lot} at {current_time}')
        for lot in lots:
            if lot > current_lot:
                running_lots.append(lot)
        try:
            next_lot = min(running_lots)
        except ValueError:
            msg = 'All lots on the watchlist have been completed'
            myobj = gTTS(text=msg, lang='en', slow=False, tld='co.uk')
            myobj.save('msg.mp3')
            pygame.mixer.init()
            pygame.mixer.music.load('msg.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(4000)
            #message = twilioCli.messages.create(body=msg, from_=myTwilioNumber, to=myCellPhone)
            sys.exit(msg)
        lots_to_nextlot = next_lot - current_lot
        if lots_to_nextlot <= 5:
            rl = f'{lots_to_nextlot} remaining to lot {next_lot}'
            myobj = gTTS(text=rl, lang='en', slow=False, tld='co.uk')
            myobj.save(f'{time_stamp}.mp3')
            pygame.mixer.init()
            pygame.mixer.music.load(f'{time_stamp}.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(3000)
            #message = twilioCli.messages.create(body=rl, from_=myTwilioNumber, to=myCellPhone)
        if next_lot - current_lot > 10:
            time.sleep(600)
        else:
            time.sleep(300)

        #

def get_currentlot():
    while True:
        try:
            webpage_response = requests.get(link)
            webpage = webpage_response.content
            soup = BeautifulSoup(webpage, "html.parser")
            return int(soup.find(attrs={'class':'data-lot'}).string)
        except AttributeError:
            errmsg = 'The program has encountered an error and will now exit'
            myobj = gTTS(text=errmsg, lang='en', slow=False, tld='co.uk')
            myobj.save('errmsg.mp3')
            pygame.mixer.init()
            pygame.mixer.music.load('errmsg.mp3')
            pygame.mixer.music.play()
            pygame.time.wait(4000)
            #message = twilioCli.messages.create(body=errmsg, from_=myTwilioNumber, to=myCellPhone)
            sys.exit(errmsg)
        except requests.exceptions.RequestException as e:
            current_time = datetime.now().strftime('%H:%M:%S')
            print(f'{current_time} - Connection Error, retrying again in 5 minutes')
            time.sleep(5 * 60)
            continue



if __name__ == "__main__":
    main()

