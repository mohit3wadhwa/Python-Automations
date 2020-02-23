import pyttsx3
import datetime
import speech_recognition as AW
import pyaudio
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[2].id)
engine.setProperty('voice', voices[0].id)


def speak(audio_msg):
    engine.say(audio_msg)
    engine.runAndWait()


def autorep():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning, Mohit")

    if hour >= 12 and hour < 18:
        speak("Good Afternoon, Mohit")

    else:
        speak("Good Evening, Mohit")

    speak("This is your assistance, John. How can I help you today?")


def get_command():
    r = AW.Recognizer()
    with AW.Microphone() as source:
        print('Listening... ')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recongnizing... ")
        query = r.Recongnize_google(audio, Language='en-in')
        print('User Says: ', query)

    except Exception as e:
        print(e)
        print('say it again')
        return "None"
    return query


if __name__ == "__main__":
    autorep()
    get_command()
