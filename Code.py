#!/usr/bin/env python
# coding: utf-8

# In[1]:


import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
import smtplib
from email.message import EmailMessage


# In[2]:


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
rate=engine.getProperty('rate')
engine.setProperty('rate',160)


# In[3]:


def speak(text):
    engine.say(text)
    engine.runAndWait()


# In[4]:


def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


# In[5]:


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me,Say again")
            return "None"
        return statement.lower()


# In[6]:



def send_email(*args):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('styuj51@gmail.com', '70v&&&&a')
    email = EmailMessage()
    email['From'] = 'styuj51@gmail.com'
    email['To'] = args[0]
    email['Subject'] = args[1]
    if len(args)==4:
        email['Cc']=email_list[cc]
    email.set_content(args[2])
    server.send_message(email)    


# In[ ]:





# In[7]:


email_list = {"shiva":"styuj51@gmail.com","bharadwaj":"Bhrta00@gmail.com","personal":"styuj51@gmail.com"}
def get_email_info():
    speak('To Whom you want to send email')
    name =takeCommand()
    print(name)
    if name in email_list:
        receiver = email_list[name]
        print(receiver)
    else:
        speak("Your Sender Mail is not in Contact....Can You type mail")
        receiver = input()
        print(receiver)
    speak('What is the subject of your email?')
    subject = takeCommand()
    print(subject)
    speak('Tell me the text in your email')
    message = takeCommand()
    print(message)
    speak('You Want to add any Cc.that is Carbon copy,then add Mail for Carbon copy')
    ccres=takeCommand()
    if "no" in ccres:
        send_email(receiver,subject,message)
    else:
        cc = takeCommand()
        print(cc)
        cc=email_list[cc]
        send_email(receiver,subject,message,cc)
    speak('Hey,Your email is sent')
    speak('Do you want to send more email?')
    send_more = takeCommand()
    if 'yes' in send_more:
        get_email_info()
    else:
        speak("ThankYou,....Now we are comming out of gmail")


# In[8]:


wishMe()
if __name__=='__main__':
    speak("Tell me how can I help you now?")
    while True:
        statement = takeCommand().lower()
        if statement==0:
            speak("I an not able to hear....can you say again")
            statement = takeCommand().lower()
            

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant  is shutting down,Good bye')
            print('your personal assistant  is shutting down,Good bye')
            break
        if "send mail" in statement or "send gmail" in statement:
            get_email_info()
            time.sleep(3)
            

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            time.sleep(3)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            speak('your personal assistant  is shutting down,Good bye')
            break
        elif 'play' in statement:
            song=command.replace('play','')
            talk('Playing')
            print(song)
            pywhatkit.playonyt(song)
            break
            
        

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            speak('your personal assistant  is shutting down,Good bye')
            break

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(3)

        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")



        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            time.sleep(3)

       
        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Bharadwaj")
            print("I was built by Bharadwaj")

        elif "open stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")
            break;

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            break;

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            break;
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

time.sleep(2)


# In[ ]:





# In[ ]:




