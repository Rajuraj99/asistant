# Python Project
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)


def talk(text):
    alexa.say(text)
    alexa.runAndWait()


def take_command():
    # global command
    try:
        with sr.Microphone() as source:
            print(' Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                # print(command)
                command = command.replace('alexa', '')
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    if 'hi' in command:
        print("Hello! How can I help you?")
        talk("Hello! How can I help you?")
    elif 'hello' in command:
        print("Hello! How can I help you?")
        talk("Hello! How can I help you?")
    elif 'how are you' in command:
        talk("I am fine, And you?")
    elif 'morning' in command:
        talk("Good Morning! Have a Nice day!!")
    elif'good night' in command:
        talk("Good Night! Have a Sweet dream!!")
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print("Now time is " + time)
        talk("Now time is" + time)
    elif 'play' in command:
        video = command.replace('play', '')
        pywhatkit.playonyt(video)
    elif 'about' in command:
        look = command.replace('about', '')
        info = wikipedia.summary(look, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        jokes = pyjokes.get_jokes()
        print(jokes)
        talk(jokes)
    elif 'marry' in command:
        print("Sorry, I'm your virtual assistant. I'm in another relationship!")
        talk("Sorry, I'm your virtual assistant. I'm in another relationship!")
    else:
        talk("I did not get it! But I can search it for you..")
        pywhatkit.search(command)


while True:
    run_alexa()
