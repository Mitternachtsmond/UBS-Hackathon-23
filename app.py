from flask import Flask,render_template,url_for,redirect,request,Response
from flask_sqlalchemy import SQLAlchemy
import cgi
import cv2

app = Flask(__name__)
camera=cv2.VideoCapture(0)


#Sqlite related libraries
import sqlite3
conn = sqlite3.connect('HealthDB.db')
print ("Opened database successfully")


#For Creating Database thse commands were used

# conn.execute('CREATE TABLE UserData(email TEXT,age INTEGER,weight INTEGER ,height INTEGER ,gender TEXT,workhr INTEGER,pills_status TEXT,pills_name TEXT,pills_time time ,water INTEGER,exercise TEXT,exercisetime time nullable,hobby_status TEXT,brekfasttime time,lunchtime time,dinnertime time,sleephr INTEGER,sleeptime time)')

# conn.execute('CREATE TABLE Reminder(sno INTEGER PRIMARY KEY AUTOINCREMENT,email TEXT,logintime time,pills_time time default null,water time default null,exercisetime time default null,brekfasttime time default null,lunchtime time default null,dinnertime time default null,sleeptime time default null)')

# conn.execute('CREATE TABLE AddGoal(sno INTEGER PRIMARY KEY AUTOINCREMENT,email TEXT,logintime time,title TEXT,remindtime time,day TEXT)')


# conn.execute('CREATE TABLE UserAuth(email TEXT,uname TEXT,pwd TEXT)')
#uid ,age,weight,height,gender,workhr,pills_status,pills_name,pills_time,water,exercise,exercisetime,hobby_status,brekfasttime,lunchtime,dinnertime,sleephr,sleeptime
print ("Table created successfully")
conn.close()


#For reminder notification related libraries												
import getpass														
import schedule														
import time
import getpass	
import time
import pyttsx3
import pyjokes
from translate import Translator
import schedule														
import time
import os 
import time
from plyer import notification  

  
#Used to add reminders manually   
def addgoaltitle(title):
    notification.notify(  
    title = title+"Reminder Time!!",  
    message = "Hey , it's "+title+" and a joke. ")
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say("Hey , it's "+title+" and a joke. " )
    speakJoke()
    engine.setProperty('rate', 10)
    engine.runAndWait()

#Used for reminder of drinking water
def water():
    notification.notify(  
    title = "Water Reminder Time!!",  
    message = "Hey pretty girl , it's time to drink water. ")
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say("Hey pretty girl , it's time to drink water. ")
    engine.setProperty('rate', 10)
    engine.runAndWait()

#Used for any pills reminder
def pills():
    notification.notify(  
    title = "Pills Reminder Time!!",  
    message = "Hey pretty girl , it's time to pills and a joke. ")
    speakJoke()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say("Hey pretty girl , it's time to pills and a joke. ")
    engine.setProperty('rate', 10)
    engine.runAndWait()
    
#Used to say some jokes for fun
def speakJoke(): 
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say("And the joke is........... ,"+pyjokes.get_joke(language="en", category="neutral"))
    engine.setProperty('rate',10)
    engine.runAndWait()


#Code related to posture recognition
def generate_frames():    
    import cv2 
    import getpass

    getUser = getpass.getuser()
    save = 'C:/Users/' + getUser + "/Desktop"


    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)
    while True:
        try:
            check, frame = webcam.read()
            print(check) #prints true as long as the webcam is running
            print(frame) #prints matrix values of each framecd 
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('s'): 
                cv2.imwrite(filename='saved_img.jpg', img=frame)
                # cv2.imwrite(os.path.join(save, "user.png"), webcam)
                webcam.release()
                img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
                img_new = cv2.imshow("Captured Image", img_new)
                cv2.waitKey(1650)
                cv2.destroyAllWindows()
                print("Processing image...")
                img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                print("Converting RGB image to grayscale...")
                gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                print("Converted RGB image to grayscale...")
                print("Resizing image to 28x28 scale...")
                img_ = cv2.resize(gray,(28,28))
                print("Resized...")
                img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
                print("Image saved!")
            
                break
            elif key == ord('q'):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break
            
        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
        


    import cv2 as cv
    import matplotlib.pyplot as plt
    # import cv2_imshow


    net= cv.dnn.readNetFromTensorflow("graph_opt.pb")

    inWidth= 368
    inHeight= 368
    thr =0.2

    BODY_PARTS = { "Nose": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
                    "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
                    "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "REye": 14,
                    "LEye": 15, "REar": 16, "LEar": 17, "Background": 18 }
    POSE_PAIRS = [ ["Neck", "RShoulder"], ["Neck", "LShoulder"], ["RShoulder", "RElbow"],
                    ["RElbow", "RWrist"], ["LShoulder", "LElbow"], ["LElbow", "LWrist"],
                    ["Neck", "RHip"], ["RHip", "RKnee"], ["RKnee", "RAnkle"], ["Neck", "LHip"],
                    ["LHip", "LKnee"], ["LKnee", "LAnkle"], ["Neck", "Nose"], ["Nose", "REye"],
                    ["REye", "REar"], ["Nose", "LEye"], ["LEye", "LEar"] ]

    from skimage import io

    #img='/content/drive/MyDrive/ImageProcessing/pose.jpg"
    img = io.imread('saved_img.jpg')
    #img = cv.imread('/content/drive/MyDrive/ImageProcessing/pose.jpg')

    plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2BGRA))

    #255/2= 127.5
    def pose_estimation(frame):
        frameWidth= frame.shape[1]
        frameHeight= frame.shape[0]
        inp = cv.dnn.blobFromImage(frame, 0, (inWidth, inHeight),
                                    (0, 0, 0), swapRB=False, crop=False)
        net.setInput(inp)
        out = net.forward()

        assert(len(BODY_PARTS) <= out.shape[1])

        points = []    #list

        for i in range(len(BODY_PARTS)):
                # Slice heatmap of corresponding body's part.
                heatMap = out[0, i, :, :]

                # Originally, we try to find all the local maximums. To simplify a sample
                # we just find a global one. However only a single pose at the same time
                # could be detected this way.
                _, conf, _, point = cv.minMaxLoc(heatMap)
                x = (frameWidth * point[0]) / out.shape[3]
                y = (frameHeight * point[1]) / out.shape[2]

                # Add a point if it's confidence is higher than threshold.
                points.append((int(x), int(y)) if conf > thr else None)

        for pair in POSE_PAIRS:
                partFrom = pair[0]
                partTo = pair[1]
                assert(partFrom in BODY_PARTS)
                assert(partTo in BODY_PARTS)

                idFrom = BODY_PARTS[partFrom]
                idTo = BODY_PARTS[partTo]

                if points[idFrom] and points[idTo]:
                    cv.line(frame, points[idFrom], points[idTo], (0, 255, 0), 3)
                    cv.ellipse(frame, points[idFrom], (3, 3), 0, 0, 360, (0, 0, 255), cv.FILLED)
                    cv.ellipse(frame, points[idTo], (3, 3), 0, 0, 360, (0, 0, 255), cv.FILLED)

        t, _ = net.getPerfProfile()
        freq = cv.getTickFrequency() / 1000
        cv.putText(frame, '%.2fms' % (t / freq), (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        print('%.2fms' % (t / freq))
        value='%.2fms' % (t / freq)
        cv.imshow("saved_img.jpg",frame)
        if value <'300' or value > '400' :
            print("sit properly")
            notification.notify(  
            title = "Posture Reminder Time!!",  
            message = "Hey , please sit erect")
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.say("Hey pretty girl , it's time to drink water and a joke. ")
            engine.setProperty('rate', 10)
            engine.runAndWait()
        else:
            print("You are good")
            notification.notify(  
            title = "Posture Reminder Time!!",  
            message = "Hey , keep it up,you are good with the posture")
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[1].id)
            engine.say("Hey pretty girl , it's time to drink water and a joke. ")
            engine.setProperty('rate', 10)
            engine.runAndWait()
        cv.waitKey(5000)

        #cv2_imshow(img)
    estimated_image= pose_estimation(img)

    #plt.imshow(cv.cvtColor(estimated_image, cv.COLOR_BGR2RGB))    

@app.route('/')
def login():
    # reminder()
    return render_template('login.html')

@app.route('/home')
def home():
    # reminder()
    return render_template('home.html')

@app.route('/healthquiz')
def healthquiz():
    # reminder()
    return render_template('healthquiz.html')

#Function for adding records of user data in UserData table
@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
      try:        
         form = cgi.FieldStorage()         
         email=request.form.get('email')
         age=request.form.get('age')
         weight=request.form.get('weight')
         height=request.form.get('height')
         gender=request.form.get('gender')
         workhr=request.form.get('workhr')
         pills_status=request.form.get('pills_status')
         pills_name=request.form.get('pills_name')
         pills_time=request.form.get('pills_time')        
         water=request.form.get('water')
         exercise=request.form.get('exercise')
         exercisetime=request.form.get('exercisetime')
         hobby_status=request.form.get('hobby_status')
         brekfasttime=request.form.get('breakfasttime')
         lunchtime=request.form.get('lunchtime')
         dinnertime=request.form.get('dinnertime')
         sleephr=request.form.get('sleephr')
         sleeptime=request.form.get('sleeptime')
         from datetime import datetime
         now = datetime.now()

         logintime=now.strftime("%H:%M")

         
         with sqlite3.connect("HealthDB.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO UserData (email,age,weight,height,gender,workhr,pills_status,pills_name,pills_time,water,exercise,exercisetime,hobby_status,brekfasttime,lunchtime,dinnertime,sleephr,sleeptime) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(email,age,weight,height,gender,workhr,pills_status,pills_name,pills_time,water,exercise,exercisetime,hobby_status,brekfasttime,lunchtime,dinnertime,sleephr,sleeptime) )

            cur.execute("INSERT INTO Reminder (email,logintime,pills_time ,water ,exercisetime ,brekfasttime ,lunchtime,dinnertime ,sleeptime) VALUES (?,?,?,?,?,?,?,?,?)",(email,logintime,pills_time ,water ,exercisetime ,brekfasttime ,lunchtime,dinnertime ,sleeptime) )
            
            con.commit()
            con.close()
            #msg = "Record successfully added"
            print("\n\n !!!!!!!!!Record successfully added")

    #      with sqlite3.connect("HealthDB.db") as con:
    #         cur = con.cursor()
    #         cur.execute("INSERT INTO Reminder (email,logintime,pills_time ,water ,exercisetime ,brekfasttime ,lunchtime,dinnertime ,sleeptime) VALUES (?,?,?,?,?,?,?,?,?)",(email,logintime,pills_time ,water ,exercisetime ,brekfasttime ,lunchtime,dinnertime ,sleeptime) )
            
    #         con.commit()
    #         con.close()
    #         #msg = "Record successfully added"
    #         print("\n\n !!!!!!!!!Record successfully added")
        
    #   except Exception as e: print(e)
    #      #conn.rollback()
    #      # msg = "error in insert operation"
    #      # print("\n\n !!!!!!!!!Record not added")
      
      finally:
         return home()

#Used for rendering to register.html     
@app.route('/register')
def register():
    # reminder()
    return render_template('register.html')

#Used for rendering to addTask.html  
@app.route('/addTasks')
def addTasks():
    # reminder()
    return render_template('addTasks.html')

#Used for rendering to register.html  
@app.route('/addgoal',methods = ['POST', 'GET'])
def addgoal():
    if request.method == 'POST':
      try: 
         form = cgi.FieldStorage()
        
         
         email=request.form.get('email')
         title=request.form.get('title')
         remindtime=request.form.get('remindtime')
         day=request.form.get('day')
         print(email,title,remindtime,day)
         from datetime import datetime
         now = datetime.now()

         logintime=now.strftime("%H:%M")

         
         with sqlite3.connect("HealthDB.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO AddGoal (email,logintime,title,remindtime,day) VALUES (?,?,?,?,?)",(email,logintime,title,remindtime,day) )
            
            con.commit()
            con.close()
            #msg = "Record successfully added"
            print("\n\n !!!!!!!!!Record successfully added")

    #      with sqlite3.connect("HealthDB.db") as con:
    #         cur = con.cursor()
    #         cur.execute("INSERT INTO Reminder (email,logintime,pills_time ,water ,exercisetime ,brekfasttime ,lunchtime,dinnertime ,sleeptime) VALUES (?,?,?,?,?,?,?,?,?)",(email,logintime,pills_time ,water ,exercisetime ,brekfasttime ,lunchtime,dinnertime ,sleeptime) )
            
    #         con.commit()
    #         con.close()
    #         #msg = "Record successfully added"
    #         print("\n\n !!!!!!!!!Record successfully added")
        
    #   except Exception as e: print(e)
    #      #conn.rollback()
    #      # msg = "error in insert operation"
    #      # print("\n\n !!!!!!!!!Record not added")
      
      finally:
         return home()


#Function for adding records of user authentication details in UserAuth table
@app.route('/addUser',methods = ['POST', 'GET'])
def addUser():
  
      try:
         form = cgi.FieldStorage()
         
         email=request.form.get('Email')
         pwd=request.form.get('Password')
         
         with sqlite3.connect("HealthDB.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO UserAuth (email,uname,pwd) VALUES (?,?,?)",("ash68patel@gmail.com","","ash123") )
            
            con.commit()
            con.close()
            print("\n\n !!!!!!!!!Record successfully added")
      
      finally:
         return healthquiz()

#Function for login authentication
@app.route('/loginauth',methods=['POST', 'GET'])
def loginauth():
    return home()
    if request.method == 'POST':
      try:
         form = cgi.FieldStorage()
       
         email=request.form.get('Email')
         pwd=request.form.get('Password')
         sqliteConnection = sqlite3.connect('HealthDB.db')
         cursor = sqliteConnection.cursor()
         print("Connected to SQLite")
        #  sqlite_select_query = "SELECT * from UserAuth where email="+email+"and pwd="+pwd
         sqlite_select_query = "SELECT * from UserAuth where email='ash68patel@gmail.com'and pwd='ash123'"
         cursor.execute(sqlite_select_query)
         print(cursor.execute(sqlite_select_query))
         records = cursor.fetchone()
         
         if(records[0]==email):
             cursor.close()
             return home()
         else:
             cursor.close()
             return login()

      finally:
          return home()



#Used for rendering to mentalhealthome.html  
@app.route('/mentalhealthhome')
def mentalhealthhome():
    return render_template('mentalhealthhome.html')

#Used for rendering to videoshow.html  
@app.route('/videoshow')
def videoshow():
    return render_template('videoshow.html')


#Used for rendering to videoshow.html  
@app.route('/video')
def video():
   return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)



    #Further code is used for scheduling reminders using SQLITE
    print("Hey there....")
    print("This is a simple reminder app in python!!!")
    watermin=0
    pills_time=0
    try:
        sqliteConnection = sqlite3.connect('HealthDB.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_select_query = "SELECT * from Reminder where email='ash68patel@gmail.com'ORDER BY sno DESC LIMIT 1"
        cursor.execute(sqlite_select_query)
        records = cursor.fetchone()
        print("Connected to SQLite")

        pills_time= records[3]

        cursor.close()

        cursor = sqliteConnection.cursor()
        sqlite_select_query = "SELECT * from AddGoal where email='ash68patel@gmail.com'"
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for row in records:
            days=row[5]
            remindtime=row[4]
            title=row[3]
            print(days,remindtime,title)
            if(days=="everyday"):
                schedule.every().day.at(remindtime).do(addgoaltitle,title)
                
            else:
                schedule.every().days.at(remindtime).do(addgoaltitle,title)
                
        cursor.close()

        schedule.every().day.at(pills_time).do(pills)
        
        schedule.every(2).minutes.do(water)
        print(pills_time)
        
        while True:
            schedule.run_pending()
            time.sleep(1) 
        
        
    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    sqliteConnection.close()
    
 