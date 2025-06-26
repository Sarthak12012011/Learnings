import random
import sys
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Welcome to The Perfect Guess!")
speak("I have selected a number between 1 and 100.")
speak("Can you guess what it is?")

print("Welcome to The Perfect Guess!")
print("I have selected a number between 1 and 100.")
print("Can you guess what it is?")

you = 0
computer = 0
count = 0

def game(you, computer, count):
    computer = random.randint(1, 100)
    while you != computer:
        try:
            you = int(input("Enter your guess: "))
            count += 1
            if you > computer:
                speak("Try lower!")
                print("Try lower!")
            elif you < computer:
                speak("Try higher!")
                print("Try higher!")
        except ValueError:
            speak("Invalid input, please enter a number.")
            print("Invalid input, please enter a number.")
            continue
        
        if count % 10 == 0:
            speak("You have used 10 attempts.")
            b = input('Out of tries!!! Would you like to try again? (yes/no): ')
            if b.lower() == 'no':
                speak("Thanks for playing!")
                sys.exit("Thanks for playing!")
            elif b.lower() == 'yes':
                game(you, computer, count)
            else:
                speak("Invalid input, exiting the game.")
                sys.exit("Invalid input, exiting the game.")
    
    speak(f"Congratulations! You've guessed the number {computer}.")
    print(f"Congratulations! You've guessed the number {computer}.")
    speak(f"You took {count} attempts to guess the number.")
    print(f"You took {count} attempts to guess the number.")
    speak("Would you like to play again?")
    
    you = input('Would you like to play again? (yes/no): ')
    if you.lower() == 'no':
        speak("Thanks for playing!")
        sys.exit("Thanks for playing!")
    elif you.lower() == 'yes':
        game(you, computer, count)
    else:
        speak("Invalid input, exiting the game.")
        sys.exit("Invalid input, exiting the game.")

game(you, computer, count)