from random import choice
import pyttsx3 

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def get_random_quote():
    speak("Here is a random quote for you:")
    speak(quote := choice(quotes))
    return quote

quotes = [
    "The best way to get started is to quit talking and begin doing.",
    "Don't let yesterday take up too much of today.",
    "It's not whether you get knocked down, it's whether you get up.",
    "If you are working on something exciting, it will keep you motivated.",
    "Success is not in what you have, but who you are.",
    "The harder you work for something, the greater you'll feel when you achieve it.",
    "Dream bigger. Do bigger.",
    "Don’t watch the clock; do what it does. Keep going.",
    "Great things never come from comfort zones.",
    "Push yourself, because no one else is going to do it for you.",
    "Success doesn’t just find you. You have to go out and get it.",
    "The key to success is to focus on goals, not obstacles.",
    "Dream it. Believe it. Build it.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Wake up with determination. Go to bed with satisfaction.",
    "Do something today that your future self will thank you for.",
    "Little things make big days.",
    "It’s going to be hard, but hard does not mean impossible.",
    "Don’t wait for opportunity. Create it.",
    "Sometimes we’re tested not to show our weaknesses, but to discover our strengths.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Creativity is intelligence having fun.",
    "What you lack in talent can be made up with desire, hustle, and giving 110% all the time.",
    "Do what you can with all you have, wherever you are.",
    "Develop an ‘attitude of gratitude’. Say thank you to everyone you meet for everything they do for you.",
    "You are never too old to set another goal or to dream a new dream.",
    "To see what is right and not do it is a lack of courage.",
    "Reading is to the mind, as exercise is to the body.",
    "Fake it until you make it! Act as if you had all the confidence you require until it becomes your reality.",
    "The future belongs to the competent. Get good, get better, be the best!",
    "For every reason it’s not possible, there are hundreds of people who have faced the same circumstances and succeeded.",
    "Things work out best for those who make the best of how things work out.",
    "A room without books is like a body without a soul.",
    "I find that the harder I work, the more luck I seem to have.",
    "Don’t be afraid to give up the good to go for the great.",
    "If you cannot do great things, do small things in a great way.",
    "You don't have to be great to start, but you have to start to be great.",
    "The successful warrior is the average man, with laser-like focus.",
    "There are no limits to what you can accomplish, except the limits you place on your own thinking.",
    "Motivation gets you going, but discipline keeps you growing.",
    "If you really want to do something, you'll find a way. If you don't, you'll find an excuse.",
    "Act as if what you do makes a difference. It does.",
    "Hardships often prepare ordinary people for an extraordinary destiny.",
    "Opportunities don't happen. You create them."
]



if __name__ == "__main__":
    print(get_random_quote())
    user_question = input("Would you like to hear another quote? (yes/no): ").strip().lower()
    while user_question == 'yes':
        print(get_random_quote())
        user_question = input("Would you like to hear another quote? (yes/no): ").strip().lower()
    user_quote = input('Would you like to add your own quote? (yes/no): ').strip().lower()
    if user_quote == 'yes':
        new_quote = input("Please enter your quote: ")
        quotes.append(new_quote)
        speak("Your quote has been added successfully!")
    else:
        speak("No problem, have a great day!")
    speak("Thank you for using the Random Quote Generator!")