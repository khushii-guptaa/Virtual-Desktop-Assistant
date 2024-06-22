import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import urllib.parse
import datetime
import requests
import pywhatkit as kit
import json
import twilio
import wikipedia
import cv2
import wolframalpha
import random
import tkinter as tk
import os
import winshell
import pyjokes
import feedparser
import smtplib
import time
import shutil
from twilio.rest import Client
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

# Initialize speech recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()


voiceEngine = pyttsx3.init('sapi5')
voices = voiceEngine.getProperty('voices')
voiceEngine.setProperty('voice', voices[1].id)

def startVoiceAssistant():
    # Add your voice assistant functionality here
    print("Voice Assistant Started")  # Placeholder for voice assistant logic

# Create the main window

root = tk.Tk()
root.title("Voice Assistant")
root.geometry('600x400')
root.config(bg='LightBlue1')

# Welcome message label
welcome_label = tk.Label(root, text='Welcome to the Voice Assistant', bg='LightBlue1', fg='black', font=('Courier', 15))
welcome_label.place(x=50, y=80)

# Start button
start_button = tk.Button(root, text="Start", bg='gray', font=('Courier', 15), command=startVoiceAssistant)
start_button.place(x=250, y=200)

# def close_start_button():
#     close_start_button.destroy()
# Command display label

command_label = tk.Label(root, text="Command: ", bg='LightBlue1', fg='black', font=('Courier', 15))
command_label.place(x=50, y=150)

# Runs the window till it is closed
root.mainloop()



def speak(text):
    voiceEngine.say(text)
    voiceEngine.runAndWait()


def wish():
    print("Wishing.")
    time = int(datetime.datetime.now().hour)
    global uname, asname
    if time >= 0 and time < 12:
        speak("Good Morning sir or madam!")

    elif time < 18:
        speak("Good Afternoon sir or madam!")

    else:
        speak("Good Evening sir or madam!")

    asname = "Jasper 1 point o"
    speak("I am your Voice Assistant ,")
    speak(asname)
    print("I am your Voice Assistant,", asname)


def getName():
    global uname
    speak("Can I please know your name?")
    uname = takeCommand()
    print("Name:", uname)
    speak("I am glad to know you!")
    columns = shutil.get_terminal_size().columns
    speak("How can i Help you, ")
    speak(uname)


def takeCommand():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening to the user")
        recog.pause_threshold = 1
        try:
            userInput = recog.listen(source, timeout=5)
        except sr.WaitTimeoutError:
            print("Timeout occurred while listening.")
            return "None"

    try:
        print("Recognizing the command")
        command = recog.recognize_google(userInput, language='en-in')
        print(f"Command is: {command}\n")
        if 'stop' in command.lower():  # Stop command to exit the loop
            return "stop"
    except Exception as e:
        print(e)
        print("Unable to Recognize the voice.")
        return "None"

    return command

def capture_image():
    camera = cv2.VideoCapture(0)  # Access the default camera (0 for the first/default camera)

    if not camera.isOpened():
        print("Error: Could not open camera")
        return

    ret, frame = camera.read()  # Capture frame-by-frame

    if not ret:
        print("Error: Failed to capture image")
        camera.release()
        return

    # Save the captured image to a file
    cv2.imwrite('captured_image.jpg', frame)
    print("Image captured and saved as captured_image.jpg")

    camera.release()  # Release the camera

    # Open the saved image using the default image viewer
    os.startfile('captured_image.jpg')

def open_website(url):
    webbrowser.open(url)


def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    open_website(url)

def sendEmail(to, content):
    print("Sending mail to ", to)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # paste your email id and password in the respective places
    server.login('7890khushigupta@gmail.com', 'password')
    server.sendmail('7890khushigupta@gmail.com', to, content)
    server.close()


def getWeather(cityName):
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"  # base url from where we extract weather report
    api_key = 'a57dbf5a22a1303e8af738e8986dde59'  # Replace 'YOUR_API_KEY_HERE' with your actual API key
    url = baseUrl + "appid=" + api_key + "&q=" + cityName
    response = requests.get(url)
    weather_data = response.json()

    # If there is no error, getting all the weather conditions
    if weather_data.get("cod") != "404":
        main_data = weather_data["main"]
        temp = main_data["temp"] - 273.15  # Convert temperature from Kelvin to Celsius
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        description = weather_data["weather"][0]["description"]
        info = (f"Temperature: {temp:.2f}°C\nAtmospheric pressure: {pressure} hPa\nHumidity: {humidity}%\nDescription: {description}")
        print(info)
        speak("Here is the weather report for")
        speak(cityName)
        speak(info)
    else:
        speak("City Not Found")



def getNews():
    try:
        response = requests.get('https://www.bbc.com/news')
        b4soup = BeautifulSoup(response.text, 'html.parser')
        headLines = b4soup.find('body').find_all('h3')
        unwantedLines = ['BBC World News TV', 'BBC World Service Radio',
                         'News daily newsletter', 'Mobile app', 'Get in touch']

        news_list = []

        for x in list(dict.fromkeys(headLines)):
            if x.text.strip() not in unwantedLines:
                news_list.append(x.text.strip())

        # Speaking the news headlines
        if news_list:
            speak("Here are the latest news headlines from BBC News.")
            for headline in news_list:
                speak(headline)
        else:
            speak("No news headlines found.")

    except Exception as e:
        print(str(e))



if __name__ == '__main__':
    # Your main code logic goes here


    uname = ''
    asname = ''
    os.system('cls')
    wish()
    getName()
    print(uname)

    while True:

        command = takeCommand().lower()
        print(command)

        if "jarvis" in command:
            wish()

        elif 'how are you' in command or "how r u" in command:
            speak("I am fine, Thank you")
            speak("How are you, ")
            speak(uname)

        elif "good morning" in command or "good afternoon" in command or "good evening" in command:
            speak("A very" + command)
            speak("Thank you for wishing me! Hope you are doing well!")

        elif 'fine' in command or "good" in command or "okay" in command:
            speak("It's good to know that your fine")

        elif "who are you" in command:
            speak("I am your virtual assistant.")

        elif "change my name to" in command:
            speak("What would you like me to call you, Sir or Madam ")
            uname = takeCommand()
            speak('Hello again,')
            speak(uname)

        elif "open website" in command:
            speak("Sure, which website would you like me to open?")
            website = takeCommand()
            if website:
                formatted_website = urllib.parse.quote_plus(website)
                open_website(f"https://www.google.com/search?q={formatted_website}")
        elif "search" in command:
            speak("What do you want to search for?")
            query = takeCommand()
            if query:
                search_web(query)

        elif "play" in command:
            kit.playonyt(command.replace('play', ''))

        elif "change name" in command:
            speak("What would you like to call me, Sir or Madam ")
            assname = takeCommand()
            speak("Thank you for naming me!")

        elif "what's your name" in command:
            speak("People call me")
            speak(assname)

        elif 'time' in command:
            strTime = datetime.datetime.now()
            curTime = str(strTime.hour) + "hours" + str(strTime.minute) + "minutes" + str(strTime.second) + "seconds"
            speak(uname)
            speak(f" the time is {curTime}")
            print(curTime)


        elif 'wikipedia' in command:

            speak('Searching Wikipedia')

            search_query = command.replace("wikipedia", "").strip()  # Remove 'wikipedia' from the command

            results = wikipedia.summary(search_query, sentences=3)

            speak("These are the results from Wikipedia")

            print(results)

            speak(results)


        elif 'open youtube' in command:
            speak("Here you go, the Youtube is opening\n")
            webbrowser.open("youtube.com")

        elif 'open google' in command:
            speak("Opening Google\n")
            webbrowser.open("google.com")


        elif 'play music' in command or 'play song' in command:

            speak("Enjoy the music!")

            music_dir = r"C:\Users\Dell\Music"  # Path to your music directory

            songs = os.listdir(music_dir)

            print(songs)

            # Check if there are any songs in the directory

            if songs:

                # Randomly select a song from the list of songs

                random_song = os.path.join(music_dir, random.choice(songs))

                os.startfile(random_song)

            else:

                speak("There are no songs in the music directory.")

        elif 'joke' in command:
            speak(pyjokes.get_joke())

        elif 'mail' in command:
            try:
                speak("Whom should I send the mail")
                to = input()
                speak("What is the body?")
                content = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent successfully !")
            except Exception as e:
                print(e)
                speak("I am sorry, not able to send this email")

        elif 'exit' in command:
            speak("Thanks for giving me your time")
            exit()

        elif "will you be my gf" in command or "will you be my bf" in command:
            speak("I'm not sure about that, may be you should give me some time")

        elif "i love u" in command:
            speak("Thank you! But, It's a pleasure to hear it from you.")

        elif "weather" in command:
            speak(" Please tell your city name ")
            print("City name : ")
            cityName = takeCommand()
            getWeather(cityName)

        elif "what is" in command or "who is" in command:

            client = wolframalpha.Client("TQK23P-PAY2GH66P7")
            res = client.query(command)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No results")

        elif 'search' in command:
            command = command.replace("search", "")
            webbrowser.open(command)

        elif 'news' in command:
            getNews()


        elif "don't listen" in command or "stop listening" in command:

            speak("For how much time do you want to stop me from listening to commands?")

            a = takeCommand()

            # Extract the numerical part of the input

            time_string = [int(s) for s in a.split() if s.isdigit()]

            # Convert the time to seconds (assuming the input contains minutes)

            if time_string:
                time_in_seconds = time_string[0] * 60  # Convert minutes to seconds

                time.sleep(time_in_seconds)

                print(f"Stopped listening for {time_string[0]} minutes")



        elif "camera" in command or "take a photo" in command or "open camera" in command:

            capture_image()

        elif 'shutdown system' in command:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif "restart" in command:
            subprocess.call(["shutdown", "/r"])

        elif "sleep" in command:
            speak("Setting in sleep mode")
            subprocess.call("shutdown / h")

        elif "write a note" in command:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
        else:
            speak("Sorry, I am not able to understand you")
