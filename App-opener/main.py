from AppOpener import open # Import necessary libraries
import pyttsx3 

engine = pyttsx3.init()
engine.setProperty('rate', 175)  # Set speech rate
engine.setProperty('volume', 1)  # Set volume level (0.0 to 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set voice to English

# Ensure the AppOpener module is installed

# Text-to-Speech Function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# App Opener Script
speak('Welcome to the App Opener!')
while True:
    speak('What app do you wish to open?')
    user_input = input("Enter the name of the app you want to open: ")
    try:
        open(user_input)
        speak(f'Opening {user_input}...')
        print(f"Opening {user_input}...")
    except Exception as e:
        speak(f"Error opening {user_input}: {e}")
        print(f"Error opening {user_input}: {e}")
    # Ask if the user wants to open another app
    speak('Do you want to open another app?')
    repeat = input("Do you want to open another app? (yes/no): ").strip().lower()
    if repeat != 'yes':
        speak('Exiting the app opener.')
        print("Exiting the app opener.")
        break
# Note: Make sure to install the required libraries using pip:
# pip install AppOpener pyttsx3
