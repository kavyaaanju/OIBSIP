import pyttsx3
import speech_recognition as sr
import datetime 
import wikipedia
import webbrowser 

def speak(audio):
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

def greetme():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")    
    speak("Hello! I am Sudha, your voice assistant. How may I help you?")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        q = r.recognize_google(audio, language='en-in')
        print(f"User said: {q}\n")
        return q.lower()
    except Exception as e:
        print(e)
        return "none"

if __name__ == "__main__":
    greetme()
    while True:
        q = listen()

        if 'wikipedia' in q:
            speak('Searching Wikipedia...')
            q = q.replace("wikipedia", "")
            try:
                results = wikipedia.summary(q, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any relevant information.")
            except wikipedia.exceptions.DisambiguationError:
                speak("There are multiple matches. Please be more specific.")

        elif 'open youtube' in q:
            webbrowser.open("https://www.youtube.com")
         

        elif 'open google' in q:
            webbrowser.open("https://www.google.com")

        elif 'the time' in q:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")

        elif 'get date' in q:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            speak(f"The current date is {current_date}")

        elif "exit" in q or "bye" in q:
            speak("Goodbye! Have a great day.")
            break

        

