import os 
import time
import pyttsx3
import pyjokes
from translate import Transl2ator

import speech_recognition as sr 
# from gtts import gTTS

from plyer import notification  
print("In reminder file ##########@@@@@@@@@@")
  
       

def speak(text):
    # text=translate(text)
    # yield text
    notification.notify(  
    title = "Reminder Time!!",  
    message = text,  
    app_icon = None,  
    timeout = 10,  
    toast = False  
    )  
    # engine = pyttsx3.init('sapi5')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.setProperty('rate', 10)
    engine.runAndWait()
    
def speakJoke(text): 
    # engine = pyttsx3.init('sapi5')
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
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

text="Hey pretty girl , it's time to drink water and a joke. "

try:  
    #   translate("Hey pretty girl , it's time to drink water and a joke. ")
     
      speak(text)
except Exception as e:
      print(e)
speakJoke("And the joke is........... ,"+pyjokes.get_joke(language="en", category="neutral"))
pyjokes.get_joke(language="en", category="neutral")








# from flask import Flask,render_template,url_for,redirect,request,Response
# # from botalgo import chatbot_response
# from flask_sqlalchemy import SQLAlchemy

# import cgi
# import cv2


# app = Flask(__name__)
# camera=cv2.VideoCapture(0)

# import sqlite3

# conn = sqlite3.connect('HealthDB.db')

# print ("Opened database successfully")

# # conn.execute('CREATE TABLE UserData(uid int Primary Key AUTOINCREMENT,email TEXT,age int ,weight int ,height int ,gender TEXT,workhr int,pills_status TEXT,pills_name TEXT,pills_time time ,water TEXT,exercise TEXT,exercisetime time nullable,hobby_status TEXT,brekfasttime time,lunchtime time,dinnertime time,sleephr int,sleeptime time)')
# #uid ,age,weight,height,gender,workhr,pills_status,pills_name,pills_time,water,exercise,exercisetime,hobby_status,brekfasttime,lunchtime,dinnertime,sleephr,sleeptime
# #  print ("Table created successfully")
# conn.close()





# # For Reminder 

# import os 
# import time
# import pyttsx3
# import pyjokes
# from translate import Translator

# import speech_recognition as sr 
# # from gtts import gTTS

# from plyer import notification 

# def reminder():
#     def speak(text):
#     # text=translate(text)
#     # yield text
#         notification.notify(  
#         title = "Reminder Time!!",  
#         message = text,  
#         app_icon = None,  
#         timeout = 10,  
#         toast = False  
#         )  
#         # engine = pyttsx3.init('sapi5')
#         engine = pyttsx3.init()
#         voices = engine.getProperty('voices')
#         engine.setProperty('voice', voices[1].id)
#         engine.say(text)
#         engine.setProperty('rate', 10)
#         engine.runAndWait()
        
#     def speakJoke(text): 
#         # engine = pyttsx3.init('sapi5')
#         engine = pyttsx3.init()
#         voices = engine.getProperty('voices')
#         engine.setProperty('voice', voices[1].id)
#         engine.say(text)
#         engine.setProperty('rate',10)
#         engine.runAndWait()


#     # def recognize():
#     # 	print("start speaking")
#     # 	r=sr.Recognizer()
#     # 	with sr.Microphone() as source:
#     # 		#lbl4=Label(newWindow,text="Speak Anything",fg="Red",font=("Times",30))
#     # 		#lbl4.place(x=170,y=90)
#     # 		audio=r.listen(source)
#     # 		try:
#     # 			text=r.recognize_google(audio)
#     # 			print(text)
                
#     # 		except:
#     # 			print()
                
#     # recognize()
    
#     # say method on the engine that passing input text to be spoken
#     #!!!!!!!!!!!!!!!!!

#     text="Hey pretty girl , it's time to drink water and a joke. "

#     try: 
#       speak(text)
#     except Exception as e:
#         print(e)
#     speakJoke("And the joke is........... ,"+pyjokes.get_joke(language="en", category="neutral"))
#     pyjokes.get_joke(language="en", category="neutral")



# def generate_frames():
#     while True:
#         #read the camera frame
#         success,frame=camera.read()
#         if not success:
#             break
#         else:
#             ret,buffer=cv2.imencode('.jpg',frame)
#             frame=buffer.tobytes()

#         yield(b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# @app.route('/')
# def login():
#     # reminder()
#     return render_template('login.html')

# @app.route('/home')
# def home():
#     # reminder()
#     return render_template('home.html')

# @app.route('/healthquiz')
# def healthquiz():
#     # reminder()
#     return render_template('healthquiz.html')


# @app.route('/addrec',methods = ['POST', 'GET'])
# def addrec():
#     if request.method == 'POST':
#       try:
         
#          # nm = request.form['nm']
#          # addr = request.form['add']
#          # city = request.form['city']
#          # pin = request.form['pin']
#          form = cgi.FieldStorage()
#          #  searchterm =  form.getvalue('searchbox')
#          # preferred_long_run_day=request.get_all('preferred_long_run_day')
         
#          email=request.form.get('email')
#          age=request.form.get('age')
#          weight=request.form.get('weight')
#          height=request.form.get('height')
#          gender=request.form.get('gender')
#          workhr=request.form.get('workhr')
#          pills_status=request.form.get('pills_status')
#          pills_name=request.form.get('pills_name')
#          pills_time=request.form.get('pills_time')        
#          water=request.form.get('water')
#          exercise=request.form.get('exercise')
#          exercisetime=request.form.get('exercisetime')
#          hobby_status=request.form.get('hobby_status')
#          brekfasttime=request.form.get('breakfasttime')
#          lunchtime=request.form.get('lunchtime')
#          dinnertime=request.form.get('dinnertime')
#          sleephr=request.form.get('sleephr')
#          sleeptime=request.form.get('sleeptime')

         
#          with sqlite3.connect("database.db") as con:
#             cur = con.cursor()
#             cur.execute("INSERT INTO UserData (email,age,weight,height,gender,workhr,pills_status,pills_name,pills_time,water,exercise,exercisetime,hobby_status,brekfasttime,lunchtime,dinnertime,sleephr,sleeptime) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(email,age,weight,height,gender,workhr,pills_status,pills_name,pills_time,water,exercise,exercisetime,hobby_status,brekfasttime,lunchtime,dinnertime,sleephr,sleeptime) )
            
#             con.commit()
#             #msg = "Record successfully added"
#             print("\n\n !!!!!!!!!Record successfully added")
#       except Exception as e: print(e)
#          #conn.rollback()
#          # msg = "error in insert operation"
#          # print("\n\n !!!!!!!!!Record not added")
      
#       finally:
#          return home()
#         #  return "Record successfully added"
#          # print (preferred_long_run_day,goal_type,always_gen_workouts,has_swimming_pool_access,has_open_water_swim_access,has_bicycle,exp_level,structured_training_comfort_level)
        

# @app.route('/register')
# def register():
#     # reminder()
#     return render_template('register.html')

# @app.route('/addTasks')
# def addTasks():
#     # reminder()
#     return render_template('addTasks.html')

# @app.route('/mentalhealthhome')
# def mentalhealthhome():
#     # reminder()
#     return render_template('mentalhealthhome.html')

# # @app.route("/bot")
# # def get_bot_response():
# #     userText = request.args.get('msg')
# #     return chatbot_response(userText)

# @app.route('/videoshow')
# def videoshow():
#     return render_template('videoshow.html')

# @app.route('/video')
# def video():
#    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

# if __name__=="__main__":
#     app.run(debug=True)




