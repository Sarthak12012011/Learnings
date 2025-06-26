import random
import sys

# Main game logic
battingorballing = {'batting', 'balling'}
a = input('Odd or eve?  ').lower()

# Toss
toss = random.randint(1, 6)

def batting(runs, runs2, goal):
    print('Start!!!')

    # First innings
    while True:
        you = int(input('Your shot: '))
        if you < 0 or you > 6:
            sys.exit('Invalid input')
        
        opponent = random.randint(0, 6)
        print(f'Computer: {opponent}')
        
        if you == opponent:
            print('Out!!!!')
            break
        else:
            runs += you

    goal = runs + 1
    print(f'Target: {goal}')

    # Second innings
    while runs2 < goal:
        you2 = int(input('Your shot: '))
        if you2 < 0 or you2 > 6:
            sys.exit('Invalid input')

        opponent2 = random.randint(0, 6)
        print(f'Computer: {opponent2}')

        if you2 == opponent2:
            print('You lose!!!')
            sys.exit('Game Over')
        else:
            runs2 += you2
    
    print('You win!!!')

def balling(runs, runs2, goal):
    print('Start!!!')

    # First innings
    while True:
        you = int(input('Your ball: '))
        if you < 0 or you > 6:
            sys.exit('Invalid input')

        opponent = random.randint(0, 6)
        print(f'Computer: {opponent}')

        if you == opponent:
            print('Wicket!!!!')
            break
        else:
            runs += opponent

    goal = runs + 1
    print(f'Target: {goal}')

    # Second innings
    while runs2 < goal:
        you2 = int(input('Your ball: '))
        if you2 < 0 or you2 > 6:
            sys.exit('Invalid input')

        opponent2 = random.randint(0, 6)
        print(f'Computer: {opponent2}')

        if you2 == opponent2:
            print('You win!!!')
            sys.exit('Game Over')
        else:
            runs2 += opponent2

    print('You lose!!!')


# Handle toss and user choices
if a == 'odd':
    toss_player = int(input('Enter your number (1-6): '))
    print(f'Computer chooses: {toss}')

    if toss_player <= 0 or toss_player > 6:
        sys.exit('Invalid input')

    if (toss_player + toss) % 2 == 1:
        print('You win the toss!')
        choice = input('Batting or balling?  ').lower()
    else:
        print('Computer wins the toss!')
        comps_choice = random.choice(list(battingorballing))
        print(f'Computer chooses: {comps_choice}')
        choice = (battingorballing - {comps_choice}).pop()

elif a == 'eve':
    toss_player = int(input('Enter your number (1-6): '))
    print(f'Computer chooses: {toss}')

    if toss_player <= 0 or toss_player > 6:
        sys.exit('Invalid input')

    if (toss_player + toss) % 2 == 0:
        print('You win the toss!')
        choice = input('Batting or balling?  ').lower()
    else:
        print('Computer wins the toss!')
        comps_choice = random.choice(list(battingorballing))
        print(f'Computer chooses: {comps_choice}')
        choice = (battingorballing - {comps_choice}).pop()

else:
    sys.exit('Invalid input')

# Initialize variables
runs = 0
runs2 = 0
goal = 0

# Execute the chosen game mode
if choice == 'batting':
    batting(runs, runs2, goal)
elif choice == 'balling':
    balling(runs, runs2, goal)
else:
    sys.exit('Invalid')


