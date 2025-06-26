import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 200)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set the voice to the first available voice

def speak(text):
    engine.say(text)
    engine.runAndWait()

def check_input(value):
    try:
         return float(value)
         
    except ValueError:
        try:
            return int(value)
        except Exception:
            print("Error: Invalid input. Please enter numbers only.")
            speak("Error: Invalid input. Please enter numbers only.")
            return None
    
def add():

    a=check_input(input("Enter the number: "))
    
    b=check_input(input("Enter second number: "))
    
    if a is None or b is None: 
        return 
    
    result = a + b
    print(f'The sum of {a} and {b} is {result:10g}')
    speak(f'The sum of {a} and {b} is {result:10g}')

def subtract():
    a = check_input(input("Enter the number from which to subtract: "))
    b = check_input(input("Enter second number with which to subtract: "))
    if a is None or b is None:
        return
    result = a - b
    print(f'The difference between {a} and {b} is {result:10g}')
    speak(f'The difference between {a} and {b} is {result:10g}')

def multiply():
    a = check_input(input("Enter the first number: "))
    b = check_input(input("Enter the second number: "))
    if a is None or b is None:
        return
    result = a * b
    print(f'The product of {a} and {b} is {result:10g}')
    speak(f'The product of {a} and {b} is {result:10g}')
    

def divide():
    try:
        a = check_input(input("Enter the dividend: "))
        b = check_input(input("Enter the divisor: "))
        if a is None or b is None:
            return
        result = a / b
        print(f'The quotient of {a} and {b} is {result:10g}')
        speak(f'The quotient of {a} and {b} is {result:10g}')
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        speak("Error: Division by zero is not allowed.")

while True:
    speak("Welcome to the calculator program. You can perform addition, subtraction, multiplication, and division.")
    user_input = input("Enter the operation you want to perform (addition, subtraction, multiplication, division): ").strip().lower()
    if user_input == 'addition':
        add()
    elif user_input == 'subtraction':
        subtract()
    elif user_input == 'multiplication':
        multiply()
    elif user_input == 'division':

        divide()
    else:
        print("Invalid operation.")
        speak("Invalid operation.")
        continue
    speak('Do you want to perform another calculation?')
    another = input("Do you want to perform another operation? (yes/no): ").strip().lower()
    if another != 'yes':
        print("Thank you for using the calculator program. Goodbye!")
        speak("Thank you for using the calculator program. Goodbye!")
        break

