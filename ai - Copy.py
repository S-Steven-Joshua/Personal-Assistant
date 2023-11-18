#python -m speech_recognition#
import virtualenv
import os
import webbrowser
import pyttsx3
import datetime
import screen_brightness_control as sbc
import pywhatkit
import random
import pyautogui
import time
import numpy
import ctypes
import winshell
import psutil
import mouse
import getpass
import speech_recognition as sr
import pyaudio
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)
engine.runAndWait()
newVoiceRate=0
engine.setProperty('rate',newVoiceRate)
pyttsx3.speak("Initializing Database")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


hour = int(datetime.datetime.now().hour)
if hour>=0 and hour<12:
    pyttsx3.speak("Good Morning!")
elif hour>=12 and hour<18:
    pyttsx3.speak("Good Afternoon!")
else:
    pyttsx3.speak("Good Evening!")
pyttsx3.speak("I am Jarvis Sir. Please tell me how may I help you")





 
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        #print("Set minimum energy threshold to {}".format(r.energy_threshold))
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        p = r.recognize_google(audio, language='en-in')
        print(f"User said: {p}\n")
    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return p



while 1:
    p=takeCommand().upper()
    




    if ("DONT" == p) or ("DON'T" == p) or ("NOPE" == p):
        pyttsx3.speak("Type Again")
        continue
    elif ("GOOGLE" == p) or   ("CHROME" == p) or ("OPEN CHROME" == p):
         pyttsx3.speak("Opening")
         pyttsx3.speak("GOOGLE CHROME")
         os.startfile("chrome")
    elif ("MICROSOFT EDGE"== p) or ("SEARCH" == p) or ("EDGE" == p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("OPENING MICROSOFT EDGE")
        os.startfile("msedge")
    elif ("OPEN SPOTIFY" == p) or ("SPOTIFY" == p):
        pyttsx3.speak("Opening")
        pyttsx3.speak(" OPENING SPOTIFY")
        os.startfile("C:\\Users\\steve\\AppData\\Roaming\\Spotify\\Spotify.exe")
    elif ("OPEN CALCULATOR" == p) or ("CALCULATOR" == p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("Opening Calculator")
        os.startfile("calc")
    elif ("OPEN BOOM 3D" == p) or ("BOOM 3D" == p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("Opening Boom 3d")
        os.startfile("boom 3d")
    elif ("OPEN CMD" == p) or ("cmd" == p):
        pyttsx3.speak("opening")
        pyttsx3.speak("Opening cmd")
        os.startfile("cmd")
    elif ("BRIGHTNESS" == p):
        a=int(input("Enter the value:"))
        print(sbc.get_brightness())
        sbc.set_brightness(a)
        print(sbc.get_brightness())
    elif ("F1" in p):
     pyttsx3.speak("Opening Formula 1 picture")
     os.startfile(r"C:\Users\steve\OneDrive\Desktop\1")
    elif ("OPEN WHATSAPP" == p) or ("WHATSAPP" == p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("Opening Whatsapp")
        os.startfile("C:\\Users\\steve\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    elif ("OPEN ZOOM" == p) or ("ZOOM" == p):
        pyttsx3.speak("opening")
        pyttsx3.speak("Opening Zoom")
        os.startfile("C:\\Users\\steve\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
    elif ("OPEN MUSIC" == p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("Opening groove music")
        os.startfile(r"C:\\Users\\steve\\Music\\Band Based Keys 1")
    elif ("OPEN WORD" == p) or ("WORD" == p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("Opening word")
        os.startfile("winword")
    elif ("OPEN EXCEL" == p) or ("EXCEL" == p):
        pyttsx3.speak("opening")
        pyttsx3.speak("Opening excel")
        os.startfile("excel")
    elif ("OPEN POWERPOINT" == p) or ("POWERPOINT" == p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("Opening Power point")
        os.startfile("powerpnt")
    elif ("OPEN CMD" == p)or ("CMD" == p):
        pyttsx3.speak("opening")
        pyttsx3.speak("OPening cmd")
        os.startfile("cmd")
    elif ("OPEN YOUTUBE" == p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com/")
    elif ("OPEN TOPPER" == p) or ("TOPPER" == p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("Opening Topper os")
        webbrowser.open("https://teach.practically.com/webapp/myClassRoom.php")
    elif ("SHUTDOWN" == p):
        pyttsx3.speak("Running AI Shutdown  protocol")
        
        print("1. Shutdown Computer Immediately")
        print("2. Shutdown Computer after Given Time")
        print("3. Restart Computer Immediately")
        print("4. Restart Computer after Given Time")
        print(end="Enter Your Choice: ")
        choice = int(input())

        if choice==1:
            os.system("shutdown /s /t 0")
        elif choice==2:
            print(end="Enter Number of Seconds: ")
            sec = int(input())
            strOne = "shutdown /s /t "
            strTwo = str(sec)
            str = strOne+strTwo
            os.system(str)
        elif choice==3:
             os.system("shutdown /r /t 0")
        elif choice==4:
            print(end="Enter Number of Seconds: ")
            sec = int(input())
            strOne = "shutdown /r /t "
            strTwo = str(sec)
            str = strOne+strTwo
            os.system(str)
        else:
            print("wrong Choice")
    
       
       
    elif ("PLAY MUSIC" in p):
        pyttsx3.speak("Playing Music")
        music_dir = "C:\\Users\\steve\\Music\\Band Based Keys 1"
        songs = os.listdir(music_dir)
        a=random.randint(1,40)    
        os.startfile(os.path.join(music_dir, songs[a]))
    elif ("VOLUME UP"in p):
        s=int(input("Enter the number of times you want to increase the volume:"))
        pyautogui.press("volumeup",s)
        pyttsx3.speak("Volume has been increased")
    elif ("VOLUME DOWN"== p):
        ss=int(input("Enter the number of times you want to decrease the volume:"))
        pyautogui.press("volumedown",ss)
        pyttsx3.speak("Volume has been decreade")
    elif ("MUTE " ==  p):
        pyttsx3.speak("Right away")
        pyautogui.press("volumemute")
    elif ("PAUSE"==p):
        pyautogui.press("playpause")
    elif ("PLAY" == p):
        pyautogui.press("playpause")
    elif ("NEXT" == p):
        pyautogui.press("nexttrack")
    elif ("BACK" == p):
        pyautogui.press("prevtrack")
    elif ("OPEN NOTEPAD" == p) or ("NOTEPAD" == p):
        pyttsx3.speak("opening")
        pyttsx3.speak("Opening Notepad")
        os.startfile("notepad")
    elif ("OPEN SYSTEM PROPERTES" == p) or ("SYSTEM PROPERTIES" == p) or("DXDIAG" == p):
        pyttsx3.speak("Accessing sensitive information")
        os.startfile("dxdiag")
    elif ("EMAIL" == p):
        pyttsx3.speak("Opening")
        pyttsx3.speak("Opening Steven's gmail account")
        webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
    elif ("SET REMINDER" == p):
        pyttsx3.speak("What shall I remind you about?")
        text=input("What shall I remind you:")
        pyttsx3.speak("In how many minutes?")
        local_time=float(input("Enter the minutes:"))
        local_time=local_time*60
        time.sleep(local_time)
        pyttsx3.speak(text)
    elif ("EXIT" == p) or ("QUIT" == p):
        pyttsx3.speak("GOODBYE")
        break
    elif ("SET ALARM" == p):
        pyttsx3.speak("At what time should I wake you up")
        local_time=float(input("Enter the hours:"))
        local_time=local_time*3600
        time.sleep(local_time)
        pyttsx3.speak("Time to Wake up")
        music_dir = "C:\\Users\\steve\\Music\\Band Based Keys 1"
        songs = os.listdir(music_dir)    
        os.startfile(os.path.join(music_dir, songs[27]))
        continue
    elif ("YOUTUBE" == p):
        pyttsx3.speak("What do you want to see in youtube")
        pywhatkit.playonyt(input("What you want to see:"))
        pyttsx3.speak("Enjoy")
    elif ("SEND A MESSAGE" == p):
        pyttsx3.speak("To whom you want to send message")
        num=str(input("Enter the number:"))
        mes=str(input("Enter the message:"))
        pywhatkit.sendwhatmsg_instantly(num,mes)
    elif ("LOCK" == p):
        pyttsx3.speak("Locking the pc")
        ctypes.windll.user32.LockWorkStation()
    elif ("EMPTY RECYCLE BIN"== p):
        pyttsx3.speak("Cleaning the pc")
        winshell.recycle_bin().empty()
    elif ("CLOSE"== p):
        def close_app(app_name):
            running_apps=psutil.process_iter(['pid','name']) #returns names of running processes
            found=False
            for app in running_apps:
                sys_app=app.info.get('name').split('.')[0].lower()
                if sys_app in app_name.split() or app_name in sys_app:
                    pid=app.info.get('pid') #returns PID of the given app if found running
                    try: #deleting the app if asked app is running.(It raises error for some windows apps)
                        app_pid = psutil.Process(pid)
                        app_pid.terminate()
                        found=True
                    except: pass
                else: pass
            if not found:
                print(app_name, "not found running")
            else:
                print(app_name,"closed")
        app_name=str(input("Enter the programe to  be closed:"))
        close_app(app_name)
        pyttsx3.speak("Closed")
    elif ("SETTINGS"==p):
        pyttsx3.speak("Opening settings")
        os.startfile("ms-settings:")
    elif ("INCOGNITO"==p):
        v=None
        c=None
        while v is None:
            v=pyautogui.locateOnScreen("C:\\Users\\steve\\OneDrive\\Desktop\\chrome.png")
            print(v)
            pyautogui.moveTo(v)
            pyautogui.rightClick(v)
        for i in range(1,2):
            c=pyautogui.locateOnScreen("C:\\Users\\steve\\OneDrive\\Desktop\\incognito.png")
            print(c)
            pyautogui.moveTo(414,637)
            pyautogui.click(410,637)
        pyttsx3.speak("Incognito Tab opened")
    elif ("STOP TAKING COMMAND"==p):
        os.system("pause")
        
       
            
            
            
            
    
            
            
      

         
            
   
        
        
        
    
    

        
        
        
    
        
    



        
        
        
        
 
