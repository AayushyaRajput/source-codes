import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import smtplib 
import time

def text():
    reco = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...") 
        reco.adjust_for_ambient_noise(source)
        audio = reco.listen(source)

        try:
            print("Recognizing...") 
            data = reco.recognize_google(audio)
            return(data)
        except sr.UnknownValueError:
            print("Not understanding")

def speech(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[0].id)
    rate = engine.getProperty("rate")
    engine.setProperty("rate",150)
    engine.say(x)
    engine.runAndWait()

def sendmail(to, content):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        # Replace with your actual email and password; ensure security!
        server.login("email", "password") 
        server.sendmail("email", to, content)
        server.close()
        speech("Email sent successfully.")
    except Exception as e:
        print(e)
        speech("Failed to send email.")


if __name__=="__main__":
    speech("Jarvis here")
    while(True):
        data1 = text().lower()

        if "jarvis" in data1:
            name = "yes sir"
            speech(name)

        elif "tell me the time" in data1:
            currenttime = datetime.datetime.now().strftime("%I:%M%p")
            speech(f"Sir the time is {currenttime}")

        elif "open youtube" in data1:
            webbrowser.open("https://www.youtube.com/")

        elif "open chrome" in data1 :
            webbrowser.open("https://www.google.co.in/")  

        elif "open stackoverflow" in data1:
            webbrowser.open("https://stackoverflow.com/")    

        elif "play a song" in data1:
            add = "D:\Music"
            listsong = os.listdir(add)  
            print(listsong)
            speech("Playing Sir")
            os.startfile(os.path.join(add,listsong[0]))

        elif "send mail" in data1: 
            try:
                speech("What should I say?")
                content = text() 
                #Replace with your actual email: ensure security! 
                to = "Emailaddress"
                sendmail(to,content)

            except Exception as e:
                print(e)
                speech("Can't able to sent mail")

        elif "exit" in data1:
            speech("Thank you sir")    
            break  

        time.sleep(0)