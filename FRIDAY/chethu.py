from email.utils import localtime
from logging import exception
from posixpath import split
from unicodedata import name
from numpy import source
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time
import pywhatkit as pwt


# voice for friday :)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning !")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon !")
    else:
        speak("Good Night!")
    speak("hello sir , im friday . how may i help you")

    """def takename():

    #takes input
    
        r=sr.Recognizer()
        with sr.Microphone() as source:
        
            print("listening .....")
            r.pause_threshold=1
            audio=r.listen(source)

    try:
        print("recognising")
        name = r.recognize_google(audio,language='en-US')
        print(f"User said: {name}\n")
     
   
    except Exception as e:
        print(e)
        print("can u say that again please")
        speak("can u say that again please")
        return "None"
    return query"""


def takecommand():
    # takes input

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening .....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognising")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")

    except Exception as e:
        print("can u say that again please")
        speak("can u say that again please")
        return "None"
    return query


def safh():
    wish()

    while True:
        print("hey")
        query = takecommand().lower()

    # logic for executing task based on query
        if 'wikipedia' in query:
            speak('searching......')
            query = query.replace('wikipedia', "")
            result = wikipedia.summary(query, sentences=2)
            speak("according to me")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("http://www.google.com/")

        elif 'play music' in query:
            music_dir = 'D:\\FRIDAY\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        # elif 'time' in query:
        #     strTime = datetime.datetime.now().strftime("%H:%M:%S")
        #     speak(f"Sir , the time is {strTime}")

        elif 'open code' in query:
            path = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        # elif 'open spotify' in query:
        #    webbrowser.open("https://open.spotify.com/?_gl=1*b32fu7*_gcl_aw*R0NMLjE2NTY5NDU1NDEuQ2owS0NRanduNHFXQmhDdkFSSXNBRk5BTWlqemloakdLZ1ZwczRHTkpKV1hVekZJcHdGdHNIWV9wUkVMaDAyZERCcGdJdl9uenhMX2hJWWFBaWJlRUFMd193Y0I.*_gcl_dc*R0NMLjE2NTY5NDU1NDEuQ2owS0NRanduNHFXQmhDdkFSSXNBRk5BTWlqemloakdLZ1ZwczRHTkpKV1hVekZJcHdGdHNIWV9wUkVMaDAyZERCcGdJdl9uenhMX2hJWWFBaWJlRUFMd193Y0I.")

        elif 'time' in query:
            localtime = str(time.asctime(time.localtime(time.time())))
            l1 = localtime.split()
            l1[0] = l1[0]+"day"
            nlocaltime = " ".join(l1)
            speak(localtime)
            print(localtime)

        elif 'on youtube' in query:
            pwt.playonyt(query)

        elif 'open bookmyshow' in query:
            webbrowser.open("https://in.bookmyshow.com/bengaluru/movies/thor-love-and-thunder/ET00302403")
        
        
        elif 'quit' in query:
            speak('thank you for using FRIDAY , please share your reviews')
            exit()
safh()