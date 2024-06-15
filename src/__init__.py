import datetime

import speech_recognition as sr
import openai as ai
import os
import webbrowser
import cv2 as cv
from playsound import playsound

name = "Rakesh"
jarvisInfo = "Hi I am Jarvis A.I. I am your personal assistant. I can do many things for you. Please tell me what you " \
             "want to do."
PASSWORD = "I love you 3000"


def speaking(text):
    os.system(f"say {text}")


def listencommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            speaking("You said: " + query)
            return query
        except Exception as e:
            return "Some Error Occurred Aniket Sir"


def next_word_after_open(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Iterate through the words
    for i in range(len(words) - 1):
        # Check if the current word is "open"
        if words[i].lower() == "open":
            # Return the next word
            return words[i + 1]

    # Return None if "open" is not found or there is no word after "open"
    return None


def clickMyPhoto():
    cam = cv.VideoCapture(0)
    result, image = cam.read()
    if result:
        cv.imshow("JarvisFrame", image)
        cv.imwrite("jarvis.png", image)
        speaking("Image Captured Successfully")
        cv.waitKey(0)
        cv.destroyWindow("JarvisFrame")
    else:
        speaking("No Image Captured, Please Try Again")


if __name__ == '__main__':
    print("Hi  Sir, I am your Personal Assistant")
    speaking("Hi Sir, I am your Personal Assistant, tell me your name please")
    name = listencommand()
    counter = 3
    while counter > 0:
        speaking("Sir, Your name is " + name + "please tell me your password to login")
        password = listencommand()
        if password.lower() == PASSWORD.lower():
            speaking("Hi " + name + " Sir, I am your Personal Assistant")
            while True:
                speaking("I am listening you Sir")
                yourWords = listencommand()
                print(yourWords)
                words = yourWords.split()
                if "shutdown Jarvis".lower() in yourWords.lower():
                    speaking("Bye Bye " + name + " Sir, I am Shutting Down")
                    exit()
                elif "time" in words:
                    time = datetime.datetime.now().strftime("%H:%M")
                    speaking(name + " Sir, The time is " + time)
                elif "about yourself".lower() in yourWords.lower():
                    speaking(jarvisInfo)
                elif "open camera".lower() in yourWords.lower():
                    clickMyPhoto()
                elif "play my music" in yourWords.lower():
                    print("playing music")
                    musicPath = "/Users/aniketshrivastav/Downloads/songPaisa.mp3"
                    os.system(f"open {musicPath}")
                elif "open".lower() in yourWords.lower():
                    site = next_word_after_open(yourWords)
                    if site is None:
                        speaking("Sorry Sir, I did not get that")
                    else:
                        speaking("Opening {x} in your browser Sir".replace("{x}", site))
                        webbrowser.open("https://www.{x}.com".replace("{x}", site))
                else:
                    speaking(yourWords + " is not a valid command")
        else:
            counter = counter - 1
            speaking("Access Denied Sir, Please Try Again")
            if counter == 0:
                speaking("Your Maximum Attempts Reached Sir, Please Contact King Aniket the Great!!!")
                exit()
