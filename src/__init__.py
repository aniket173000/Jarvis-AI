import datetime

import speech_recognition as sr
import openai as ai
import os
import webbrowser


def speaking(text):
    os.system(f"say {text}")


def listencommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='en-in')
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



if __name__ == '__main__':
    print("Hi Aniket Sir, I am your Personal Assistant")
    speaking("Hi Aniket Sir, I am your Personal Assistant")
    while True:
        speaking("I am listening you Sir")
        yourWords = listencommand()
        print(yourWords)
        words = yourWords.split()
        if "shutdown Jarvis" in yourWords:
            speaking("Bye Aniket Sir, I am Shutting Down")
            exit()
        elif "time" in words:
            time = datetime.datetime.now().strftime("%H:%M")
            speaking("Aniket Sir, The time is " + time)
        else:
            site = next_word_after_open(yourWords)
            if site is None:
                speaking("Sorry Sir, I did not get that")
            else:
                speaking("Opening {x} in your browser Sir".replace("{x}", site))
                webbrowser.open("https://www.{x}.com".replace("{x}", site))

            print(yourWords)




