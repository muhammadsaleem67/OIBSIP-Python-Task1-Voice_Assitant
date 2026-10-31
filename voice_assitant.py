import speech_recognition as sr
import pyttsx3 
import datetime
import webbrowser

# Initialize the Text-to-Speech
engine = pyttsx3.init()
engine.setProperty('rate', 170) # Adjusts speaking speed

def speak(text):
    """Converts text string into spoken audio"""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listens to the microphone and converts speech to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print(f"You said: {query}")
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. could you repeat?")
        return
    except sr.RequestError:
        speak("Network error, Please check your internet connection.")
        return ""

if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I help you today?")

    while True:
        command = listen()

        if not command:
            continue

        # 1. Greeting
        if 'hello' in command or 'hi' in command:
            speak("Hello there! What's on your mind?")

        # 2. Time and Date
        elif 'time' in command or 'date' in command:
            now = datetime.datetime.now()
            time_str = now.strftime("%I:%M %p on %B %d, %y")
            speak(f"The current time and date is {time_str}")

        # 3. Web Search
        elif 'search' in command:
            speak("What would you like me to search for?")
            search_topic = listen()
            if search_topic:
                speak(f"Opening your browser to search for {search_topic}")
                webbrowser.open(f"https://www.google.com/search?q={search_topic}")
        elif 'exit' in command or 'stop' in command:
            speak("Goodbye! Shutting Down.")
            break
