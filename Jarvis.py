import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import smtplib
from time import ctime
import smtplib
import dateaf
from youtubePlayer import youtube
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("good Afternoon")
    else :
        speak("Good Evening")
    speak("Swagatam Please tell me how may I help you")

def takeCommand():
    '''
    It takes microphone Input from the user and returns String output
    '''
    r = sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.record(source,duration=5)
    
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('swagatambhattacharjee02@gmail.com','Swagbidisha2002')
    server.close()
if __name__ == "__main__":
    pyttsx3.speak("Swag is a good boy")
    wishMe()
    # writing a infinite while loop for 
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=5)
            speak("Accorgin to Wikipedia")
            print(results)
            speak(results)
    # logic for executing task based on query
        elif 'open youtube' in query:
            wb.open('youtube.com')
        elif 'open google' in query:
            wb.open('google.com')
        elif 'open facebook' in query:
            wb.open('facebook.com')
        elif 'open Linkedin' in query:
            wb.open('Linkedin.com')
        elif 'play music' in query:
            music_dir='F:\MyMusic'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            str_time=datetime.datetime.now().str_time("%H:%M:%S")
            speak(f"Sir the time is  {str_time}")
        elif 'open code' in query:
            codePath="C:\\Users\\Swagatam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif "how are you" in query:
            speak("I am fine")
        elif "what time is it" in query:
             speak(ctime())
        elif "where is" in query:
                query = query.split(" ")
                location = query[2]
                speak("Hold on Frank, I will show you where " + location + " is.")
                os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")
        elif 'email to Swagatam' in query:
            try:
                speak('What should I say?')
                content=takeCommand()
                to="swagatambhattacharjee02@gamail.com"
                sendEmail(to,content)
                speak("email has been send")
            except Exception as e:
                print(e)
                speak("Sorry Swagatam unable to send the email")
        elif 'play video from youtube' in query:
                query=query.replace('youtube',"")
                youtube().youtube(query)
                speak("Opening youtube")       
        elif 'alarm' in query:
                dateaf.alarm(query)  
        elif 'shutdown' in query:
                speak("Shutting down")
                os.system('shutdown -s')
        elif 'goodbye' in query:
                speak("Good Bye Swagatam")
                exit()
        elif 'the time' in query:
                str_time=datetime.datetime.now().strftime("%H:%M:%S")
                print(str_time)
                speak(f"Sir the time is  {str_time}")
                