import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import datetime
import smtplib
import wikipedia
from gtts import gTTS
import os
import musiclibrary

# Initialize recognizer and text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "4f68545ae12f479f9bc7e3377b3bcf08"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def sendEmail(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('krishnakala382@gmail.com', 'XXXXXXXX')  # Replace with your actual email and password
        server.sendmail('krishnakala382@gmail.com', to, content)
        server.close()
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")   
    else:
        speak("Good Evening!")  
    speak("I am Alexa Sir. Please tell me how may I help you.")       

def processCommand(c):
    try:
        if "open google" in c.lower():
            webbrowser.open("https://google.com")
        elif "open youtube" in c.lower():
            webbrowser.open("https://youtube.com")
        elif "open facebook" in c.lower():
            webbrowser.open("https://facebook.com")
        elif "open linkedin" in c.lower():
            webbrowser.open("https://linkedin.com")
        elif "open ai" in c.lower():
            webbrowser.open("https://chatgpt.com")
        elif c.lower().startswith("play"):
            song = c.lower().split(" ")[1]
            link = musiclibrary.music[song]
            webbrowser.open(link)
        elif "news" in c.lower():
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                for article in articles:
                    print(article['title'])
                    speak(article['title'])
        elif 'wikipedia' in c.lower():
            speak('Searching Wikipedia...')
            query = c.lower().replace("wikipedia", "").strip()
            if query:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            else:
                speak("Please specify what you want to search on Wikipedia.")
        elif 'email' in c.lower():
            try:
                speak("To whom should I send the email?")
                with sr.Microphone() as source:
                    audio = sr.Recognizer().listen(source)
                    to = sr.Recognizer().recognize_google(audio).replace(" ", "").lower() + "@gmail.com"  # Assuming all emails are Gmail, adapt as needed
                
                speak("What should I say?")
                with sr.Microphone() as source:
                    audio = sr.Recognizer().listen(source)
                    content = sr.Recognizer().recognize_google(audio)
                
                if sendEmail(to, content):
                    speak("Email has been sent!")
                else:
                    speak("Sorry, I am not able to send this email.")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email.")    
        else:
            speak("No query matched.")
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("An error occurred while processing your request.")

if __name__ == "__main__":
    speak("Calling Alexa...")
    wishMe()
    while True:
        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=5)
            word = r.recognize_google(audio)
            if word.lower() == "alexa":
                speak("Yes")
                with sr.Microphone() as source:
                    print("Alexa active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(f"User said: {command}")
                    processCommand(command)
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            speak("Sorry, I'm having trouble reaching the speech recognition service.")
        except Exception as e:
            print(f"An error occurred: {e}")
            speak("An error occurred while processing your request.")
