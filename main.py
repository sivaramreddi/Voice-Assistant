import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import wikiquote
import googletrans

# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def quotation():
    print(wikiquote.quote_of_the_day())
    speak(wikiquote.quote_of_the_day())


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1.0)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        
        query = r.recognize_google(audio, language='en-US')

        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didn't understand")
        return "None"
    return query


if __name__ == '__main__':

    speak("Amigo assistance activated ")
    speak("How can i help you, Sir")
    while True:
        query = take_command().lower()
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            work = query.replace("wikipedia", "")
            results = wikipedia.summary(work, sentences=5)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'moral' in query:
            quotation()
        elif 'who are you' in query:
            speak("I am amigo assistant developed by Chandrasekhar")
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        elif "time" in query:
            now = datetime.datetime.now()
            speak(f"The current time is {now.hour}:{now.minute}")
            print(f"The current time is {now.hour}:{now.minute}")
        elif 'search' in query or 'play' in query:

            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("https://youtube.com/")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("https://google.com/")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("https://github.com/")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("https://stackoverflow.com/")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("https://spotify.com/")
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            webbrowser.open("https://web.whatsapp.com/")
        elif 'open ai' in query:
            speak("opening chat gpt")
            webbrowser.open("https://chat.openai.com/")
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif "open mail" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif "translate" in query:
            translator = googletrans.Translator()
            lang = ['en', 'ta', 'te', 'kn', 'ml', 'hi']
            # To Print all the languages that Google Translator Support
            # Command to print Languages Supported
            # print(googletrans.LANGUAGES)
            speak("please tell me the Sentence that you want me to translate")
            text = take_command().lower()
            speak(
                "Please choose a Source Language by pressing a number from the following List!")
            print(
                "English --->  1  Tamil ---> 2  Telugu ---> 3  Kannada ----> 4  Malayalam ---> 5  Hindi ---> 6")
            numberS = int(input("Enter here: "))
            speak(
                "Please choose a Destination Language by pressing a number from the following List!")
            print(
                "English --->  1  Tamil ---> 2  Telugu ---> 3  Kannada ----> 4  Malayalam ---> 5  Hindi --> 6")
            numberD = int(input("Enter here: "))
            translated = translator.translate(
                text, src=lang[numberS - 1], dest=lang[numberD - 1])
            print(translated.text)

        elif 'Orion D' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
        elif 'sleep' in query:
            speak("Ok Bye. Have a nice day, sir.")
            exit(0)
