import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener =sr.Recognizer()
engine =pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices [1].id)

mango=pyttsx3.init()
mango.say('i am your alexa  ')
mango.say('what can i do for you')
mango.runAndWait()

def talk(text):

 engine.say(text)
 engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice =listener.listen(source)
            command =listener.recognize_google(voice)
            command=command.lower()
        if 'alexa' in command:
           command =command.replace('alexa','')
           print(command)
           talk(command)
    except:
        pass
    return command

def run_alexa():
    command =take_command()
    print(command)
    if'play'in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)
    elif 'information' in command:
        person = command.replace('information', '')
        info =wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, i am busy for doing my work')
    elif 'are you single ' in command:
        talk('i am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('could you say that again  i did not quite hear you')

while True:
    run_alexa()
