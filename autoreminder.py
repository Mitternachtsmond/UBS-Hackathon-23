'''
Python based voice reminder app.
Image sources :
	1. https://www.clipartmax.com/middle/m2i8K9H7K9Z5H7K9_cup-clipart-silhouette-coffee-cup-clip-art/
	2. Pngguru.com.
'''

 
#Import the necessary packages
# import notify2 														# pip3 install notfiy2
import getpass														# get the name of the system
# import os
import schedule														#pip3 install schedule
import time

import os 
import time
import pyttsx3
import pyjokes
from translate import Translator

import speech_recognition as sr 
# from gtts import gTTS

from plyer import notification  
print("In reminder file ##########@@@@@@@@@@")
  
       

def water():
    # text=translate(text)
    # yield text
    notification.notify(  
    title = "Water Reminder Time!!",  
    message = "Hey pretty girl , it's time to drink water and a joke. ")
    # engine = pyttsx3.init('sapi5')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say("Hey pretty girl , it's time to drink water and a joke. ")
    engine.setProperty('rate', 10)
    engine.runAndWait()

def seat():
    # text=translate(text)
    # yield text
    notification.notify(  
    title = "Seat Straight!!",  
    message = "Hey pretty girl , please seat straight")
    pyjokes.get_joke(language="en", category="neutral",  
    app_icon = None,  
    timeout = 10,  
    toast = False  
    )  
    # engine = pyttsx3.init('sapi5')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say("Hey pretty girl , please seat straight")
    engine.setProperty('rate', 10)
    engine.runAndWait()
    

def speakJoke(): 
    # engine = pyttsx3.init('sapi5')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say("And the joke is........... ,"+pyjokes.get_joke(language="en", category="neutral"))
    engine.setProperty('rate',10)
    engine.runAndWait()


# def recognize():
# 	print("start speaking")
# 	r=sr.Recognizer()
# 	with sr.Microphone() as source:
# 		#lbl4=Label(newWindow,text="Speak Anything",fg="Red",font=("Times",30))
# 		#lbl4.place(x=170,y=90)
# 		audio=r.listen(source)
# 		try:
# 			text=r.recognize_google(audio)
# 			print(text)
			
# 		except:
# 			print()
	         
# recognize()
 
# say method on the engine that passing input text to be spoken
#!!!!!!!!!!!!!!!!!
							# show the notification to the user.
	
if __name__=="__main__":											
	# wish()
	print("Hey there....")
	print("This is a simple reminder app in python!!!")
	# we schedule for every one hour to make a notification related to drink water.
	# schedule.every().hour.do(water)					    
	# for every 35 minutes we schedule the user to take a break
	schedule.every(1).minutes.do(water)					    
	schedule.every(2).minutes.do(seat)	
    				    	
	while True:
		schedule.run_pending()
		time.sleep(1)	