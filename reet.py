import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import pyjokes

email_set = {'name':'email'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour <12:
        speak("Good Morning ,Viraj")
    elif hour>=12 and hour<18:
        speak("Good Afternoon ,Viraj")
    elif hour>=18 and hour<21:
        speak("Good Evening, Viraj")
    else:
        speak("Good Night, viraj")
    speak("I am FRIDAY sir , Please tell me how may i help you")

def takeCommand():
    # It takes  microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1 # for it take pause of 1 sec
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Sir, you just said :{query}\n")
    except Exception as e:
        print(e)
        speak("Sorry sir, Say that again please..")
        #print("Sorry sir, Say that again please..")
        return  "None"
    return  query
def playMusic():
    music_dir = r"C:\songs"  # \\ for esaping characters
    songs = os.listdir(music_dir)
    print(*songs, sep="\n")
    # selected_song=input("Which song you want to play:"
    i = random.randint(0, len(songs) - 1)
    os.startfile(os.path.join(music_dir, songs[i]))
def AboutMe():
    speak("I am friday,Viraj Personal AI assistant created on 11th of june at 19:08:22")
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('aireet312@gmail.com','reet12375@')
    server.sendmail('vpersonal@gmail.com',to,content)
    server.close()
def conversation():
    speak("yes ,Sure i m friday,how are you")
    command = takeCommand().lower()
    if 'not good' in command:
        speak("can i do something to fix your mood..")
        command = takeCommand().lower()
        if 'no' in command:
            speak('ok,sir')
        elif 'yes' in command:
            speak("here comes a joke..")
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)
    elif 'good' in command:
        speak("Thats nice sir,what is up sir..")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia.....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)#for first 2 sentences in that searh
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            playMusic()
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath ="C:\\Users\\viraj\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'open vlc' in query:
            vlcPath=r"C:\Program Files\VideoLAN\VLC\vlc.exe"
            os.startfile(vlcPath)
        elif 'send email' in query:
            try:
                speak("Who you want to send: ")
                name = takeCommand().lower()
                speak("What should I say")
                content= takeCommand()
                to = email_set[name]
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir,i am not able to send this Email")

        elif 'terminate' in query:
            speak("termination initiated,terminating....")
            exit()

        elif 'about you' in query:
            AboutMe()

        elif 'can we talk' in query:
            conversation()


