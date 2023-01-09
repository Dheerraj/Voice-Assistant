import pyttsx3 # text to speech 
import datetime # time and date k liye
import speech_recognition as sr #khud ki voice ko pakadne k liye
import wikipedia # wikipedia se kuch lene k liye
import webbrowser #web ko open kanrne k liye
from selenium import webdriver # apne aap opne krne k liye new tab me
import os # pc k andar se kuch kholne k liye
engine=pyttsx3.init() #engine name se module ko initilise kiya hai 
voices=engine.getProperty('voices') # pc ki voice set krne k liye 
rate=engine.getProperty('rate') #speed set krne k liye 
engine.setProperty('rate',180) # yha spped set kr di 

engine.setProperty('voice',voices[0].id) # male ya female ki voice k liye

def speak(audio):  # pc sunega
    engine.say(audio) #bolne k liye
    engine.runAndWait() # run karayega
def wishMe(): # isme ye time k anusar wish krega
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("good evening")
    speak("Hello Dheeraj, how may I help you")
def takecommand():  # 
    r=sr.Recognizer() #isse ye hamari voice lega
    with sr.Microphone() as source: #use the default microphone as the audio source
        print("Listening....")
        r.pause_threshold=1  #non-speaking or there is no more audio input
        audio=r.listen(source)#listen for the first phrase and extract it into audio data


    try:
        print("Recognizing....")
        query=r.recognize_google(audio) #sunega and recognize karega
        print("User said:",query)
    except Exception as e: #nhi sun paya to
        print(e)


        print("say that again please....")
        return "None"
    return query

    
if __name__ == "__main__":
    wishMe()
   
    if 1: 
        query=takecommand().lower() #query chalai h aur lower me liya h 
        if 'wikipedia' in query: # agr mene jo bola usme wikipedia aaya 
            speak('searching wikipedia...')
            query=query.replace("wikipedia","") #query replace by wikipedia query me aa jayega wikipedia ka data
            results=wikipedia.summary(query,sentences=2) #jo search krenge wo isme store ho jayega 2 number of lines
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open google' in query:
            webbrowser.open("http://google.com")
            
        elif 'open youtube' in query:
            webbrowser.open("http://youtube.com")
            
        elif 'open wikipedia' in query:
            webbrowser.open("http://wikipedia.com")
            
        elif 'open map' in query:
            webbrowser.open("https://www.google.com/maps/@31.2444468,75.7022453,15z")
            
        elif 'open flipkart' in query:
            webbrowser.open("http://flipkart.com")
            
        elif 'show me nearest charging station' in query:
            webbrowser.open("https://www.google.com/maps/search/Gas/@31.2444418,75.6759806,13z/data=!3m1!4b1")
            
            
        elif 'tell me your status' in query:
            strTime=datetime.datetime.now().strftime("%H   %M")
            speak(f"car battery is 20% and temp of the car is 25 degree celsius and time is{strTime} PM")
            
        elif 'open notes' in query:
            #os.system("open /Applications/Google\ Chrome.app")
            os.system("open /System/Applications/Notes.app")
            
        elif 'play music' in query:
            os.system("open /Users/dheerajkasaniya/Downloads/0125.\ Imagination\ -\ AShamaluevMusic.mp3 ")
            
        elif 'open Siri' in query:
            os.system("open /System/Applications/Siri.app")
            
        elif 'open mail' in query:
            os.system("open /System/Applications/Mail.app")
            
        elif 'open my photo' in query:
            os.system("open  /Users/dheerajkasaniya/Desktop/IMG_1362.HEIC")
                
        
        elif 'open tv' in query:
            os.system("open /System/Applications/TV.app")
        
        
            
        elif 'open text edit' in query:
            os.system("open /System/Applications/TextEdit.app")
            
        elif 'play any song' in query:
            os.system("open /Users/dheerajkasaniya/Downloads/WhatsApp\ Audio\ 2021-11-30\ at\ 5.49.57\ PM.mpeg")    
        
        elif 'open stocks' in query:
            os.system("open /System/Applications/Stocks.app")
            
       
        elif 'what is my name' in query:
            speak("Dheeraj")
            
        elif 'covid status' in query:
            webbrowser.open('https://www.worldometers.info/coronavirus/')
        else:
            speak("sorry i did not get ")
            



