import pyttsx3
import random
import sys
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def game(comp):
    comp=random.choice(list(options))
    speak("Enter your choice, Rock, Paper or Scissors")
    engine.runAndWait()
    a=input("Enter your choice: \n 1. Rock \n 2. Paper \n 3. Scissors \n : ").lower()
    
    if a in options:
        speak(f"So you chose {a}")
        engine.runAndWait()
        print("Your choice: ",a)
        speak(f"Computer's choice is {comp}")
        engine.runAndWait()
        print("Computer's choice: ",comp)
        if a==comp:
            speak("It's a tie!")
            engine.runAndWait()
            return "It's a tie"
        elif a=='rock':
            if comp=='paper':
                speak("Computer wins!")
                engine.runAndWait()
                return "Computer wins!"
            else:
                speak("You win!")
                engine.runAndWait()
                return "You win!"
        elif a=='paper':
            if comp=='scissors':
                speak("Computer wins!")
                engine.runAndWait()
                return "Computer wins!"
            else:
                speak("You win!")
                engine.runAndWait()
                return "You win!"
        elif a=='scissors':
            if comp=='rock':
                speak("Computer wins!")
                engine.runAndWait()
                return("Computer wins!")
            else:
                speak("You win!")
                engine.runAndWait()
                return ("You win!")
                
    else:
        speak('Invalid input, exiting the game.')
        engine.runAndWait()
        sys.exit('Invalid input, exiting the game.')
def repeat(b):

    speak('Wanna play again?')
    engine.runAndWait()
    b=input('\nWanna play again? (yes/no): ').lower()
    
    if b=='yes':
        speak('NEW ROUND!!!!')
        engine.runAndWait()
        print('\n\tNEW ROUND\t\n')
        print(game(comp))
        print(repeat(b))
    elif b=='no':
        speak('Hope you had fun!!!')  
        engine.runAndWait()
        return 'Hope you had fun!!!!' 
    else:
        speak('Invalid input. Exiting the game')
        engine.runAndWait()
        return "Invalid input\nExiting the game"
options={'rock','paper','scissors'}
comp= None
speak("Welcome to Rock,Paper,Scissors by the one and only Sarthak Bera!")
engine.runAndWait()
print("Welcome to Rock, Paper, Scissors by the one and only Sarthak Bera!")
a= None
print(game(comp))
b=None
print(repeat(b))


