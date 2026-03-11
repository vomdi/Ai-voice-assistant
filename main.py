import ctypes
import datetime
import subprocess
import time
import webbrowser
from tkinter import *

import cv2
import googlesearch
import playsound
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
import winshell
from gtts import gTTS
from pygame import mixer
from selenium import webdriver

l = cv2.waitKey(0)
root = Tk()
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.setProperty("rate", 170)
    engine.say(text)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except sr.UnknownValueError:
            talk("Sorry, I did not get that. Try asking again.")
        except sr.RequestError:
            talk("Sorry, the service is not available")
    return said.lower()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def alexa():
    while True:
        clear = take_command()
        if 'alexa' in clear:
            talk('How can I help you?')
            run_alexa()
        else:
            time.sleep(1)
            continue

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'open game' in command:
        talk('OK. Opening game.')
        talk('Press space to make character go up. Don''t let character touch the pipes')
    elif 'open laptop' in command:
        talk('OK')
        pyautogui.press('space')
        pyautogui.moveTo(958, 652, duration=1)
        pyautogui.click()
        pyautogui.moveTo(985, 711, duration=1)
        pyautogui.click()
        pyautogui.typewrite('11129')
    elif 'lock computer' in command:
        talk('OK')
        ctypes.windll.user32.LockWorkStation()
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        from datetime import date
        today = date.today()
        print("Today's date is ", today)
        t = ("Today's date is ", today)
        talk(t)
    elif 'joke' in command:
        talk(pyjokes.get_jokes())
    elif 'search for links' in command:
        from googlesearch import search

        query = command

        for i in search(query, tld="co.in", num=10, stop=10, pause=2):
            print(i)
    elif 'hi' in command:
        print('Hi. Ask me anything')
        talk('Hi. Ask me anything')
    elif 'youtube' in command:
        talk("What do you want to search on youtube?")
        keyword = get_audio()
        if keyword != '':
            url = f"https://www.youtube.com/results?search_query={keyword}"
            webbrowser.get().open(url)
            talk(f"Here is what I found on youtube for {keyword}.")
    elif 'thanks' in command:
        talk("You are so welcome")
    elif 'bye' in command:
        print('Bye. Have a great day.')
        talk('Bye. Have a great day.')
        exit()
    elif 'open notepad' in command:
        talk('OK')
        subprocess.Popen("C:\\Windows\\System32\\notepad.exe")
        pyautogui.moveTo(997, 453, duration=1)
        pyautogui.click()
        talk('what would you like to type?')
    elif 'close notepad' in command:
        talk('OK')
        subprocess.run('Taskkill /IM notepad.exe /F', shell=True)
    elif 'open camera' in command:
        talk('OK')
        subprocess.run('start microsoft.windows.camera:', shell=True)
    elif 'video' in command:
        subprocess.run('start microsoft.windows.camera:', shell=True)
        pyautogui.moveTo(1665, 459, duration=2)
        pyautogui.click()
        pyautogui.moveTo(1670, 543, duration=2)
        talk('stop the video when you want')
        pyautogui.click()
    elif 'picture' in command:
        subprocess.run('start microsoft.windows.camera:', shell=True)
        pyautogui.moveTo(452, 553, duration=2)
        pyautogui.click(clicks=2)
        pyautogui.moveTo(1670, 543, duration=2)
        pyautogui.click()
    elif 'close camera' in command:
        talk('OK')
        subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)
    elif 'open firefox' in command:
        talk('OK')
        subprocess.Popen("C:\\Windows\\System32\\firefox.exe")
    elif 'close firefox' in command:
        talk('OK')
        subprocess.run('Taskkill /IM firefox.exe /F', shell=True)
    elif 'new tab' in command:
        talk("OK")
        pyautogui.hotkey('ctrlleft', 't')
    elif 'close tab' in command:
        talk('OK')
        pyautogui.hotkey('ctrlleft', 'w')
    elif 'google' in command:
        talk("what would you like to search on google?")
        query = get_audio()
        if query != '':
            url = f"https://www.google.com/search?q={query}"
            webbrowser.get().open(url)
            talk(f"Here is what I found on google for {query}.")
    elif 'goodnight' in command:
        print("Good night. Sleep tight. Don't let the bed bugs bite.")
        talk("Good night. Sleep tight. Don't let the bed bugs bite.")
    elif 'what is your name' in command:
        print("My name is what ever your imagination names me. But I prefer, Alexa.")
        talk("My name is what ever your imagination names me. But I prefer, Alexa.")
    elif 'stop' in command:
        talk("My pleasure")
        exit()
    elif 'call' in command:
        talk('ok')
        url = f"https://www.whatsapp.com/"
        webbrowser.get().open(url)
    elif 'weather' in command:
        talk('here is the weather today.')
        web = f"https://weather.com/weather/today/l/33.01,-97.27?par=google"
        webbrowser.get().open(web)
    else:
        talk('Please say the command again.')


while True:
    alexa()
