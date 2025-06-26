import pyttsx3
import random
import sys

# Initialize Text-to-Speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 180)  # Set speech rate
engine.setProperty('volume', 1)  # Set volume (0.0 to 1.0)

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

speak('Welcome to the Dice Roller!')
print('Welcome to the Dice Roller!')

while True:
     count = 1
     speak('How many dice do u want to roll?')
     try:
         dice_count = int(input('How many dice do you want to roll? '))
         if dice_count <= 0:
                speak('Please enter a valid number.')
                  
                continue
     except Exception:
         speak('Invalid input. Please enter a number.')
           
         continue
     dice = []
     for _ in range(dice_count):
         dice_roll = random.randint(1, 6)
         dice.append(dice_roll)
     speak(f'You rolled: {", ".join(map(str, dice))}')
       
     print(f'{count}:   You rolled: {", ".join(map(str, dice))}')
     count += 1
     speak('Do you want to roll again?')
       
     play_again=input('Do you want to roll again? (yes/no): ')
     if play_again.lower()=='no':
            speak('Thanks for playing!')
              
            sys.exit('Thanks for playing!')
     elif play_again.lower()!='yes' and play_again.lower()!='no':
            speak('Invalid input')   
              
            sys.exit('Invalid input.')
