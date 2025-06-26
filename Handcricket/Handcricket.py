import random
import sys


battingorballing={'batting','balling'}

a=input('Odd or eve?  ').lower()



toss=random.randint(1,6)

def batting(runs,runs2,goal):

    
    print('Start!!!')
    while True:
        
        you=int(input('Your shot:  '))
        if you<0 or you>6:
            
            sys.exit('invalid')
        opponent=random.randint(0,6)
        print(f'Computer:  {opponent}')
        if you==opponent:
            
            print('Out!!!!')
            break
        elif you==0:
            runs+=opponent
        else:
            runs+=you

    goal=runs+1
    print(f'Target: {goal}')


    while runs2<goal:
        
        you2=int(input('Your ball:  '))

        if you2<0 or you2>6:
            
            sys.exit('invalid')
        opponent2=random.randint(0,6)
        print(f'Computer:  {opponent2}')
        if you2==opponent2:
          
            print('Wow you won!!!!!!')
            
            sys.exit('Game over')
        if opponent2==0:
            runs2+=you2
        else:
            runs2+=opponent2


    
    print('Haha you lose!!!!!!!!')
    sys.exit('Game over')
    




def balling(runs,runs2,goal):

    
    print('Start!!!!')
    while True:
        
        you=int(input('Your ball:  '))
        if you<0 or you>6:
            
            sys.exit('invalid')
        opponent=random.randint(0,6)
        print(opponent)
        if you==opponent:
           
            print('That\'s an out!!!!!!!!')
            break
        elif opponent==0:
            runs+=you
        else:
            runs+=opponent


    goal=runs+1
    print(f'Target {goal}')
    
    while runs2<goal:
        
        you2=int(input('Your shot: '))
        if you2<0 or you2>6:
            
            sys.exit('invalid')
        opponent2=random.randint(0,6)
        print(f'Computer:  {opponent2}')
        if you2==opponent2:
            
            print('Haha you lose!!!!!')
            sys.exit('Game over')
        elif you2==0:
            runs2+=opponent2
        else:
            runs2+=you2
    

    
    print('Wow you won!!!!!')
    
    sys.exit('Game over')
        
    



if a=='odd':
    
    toss_player=int(input('Enter the number(1-6):  '))
    
    print(f'Computer chooses  {toss}')
    if toss_player<=0 or toss_player>6:
        
        sys.exit('Invalid input')
    else:
        if (toss_player+toss)%2==1:
            
            print('You win!')
            
            choice=input('Batting or balling?  ')
            choice=choice.lower()
            
            
        else:
            
            print('Computer wins!')
            comps_choice=random.choice(list(battingorballing))
            
            print(f'Computer chooses:  {comps_choice} ')
            choice=(battingorballing-{comps_choice}).pop()
elif a=='eve':
    
    toss_player=int(input('Enter the number  '))
    
    print(f'Computer chooses  {toss}')
    if toss_player<=0 or toss_player>6:
        
        sys.exit('Invalid input')
    else:
        if (toss_player+toss)%2==0:
            print('You win!')
            choice=input('Batting or balling?  ').lower()
            
            
        else:
            print('Computer wins!')
            comps_choice=random.choice(list(battingorballing))
            
            print(f'Computer chooses   {comps_choice} ')
            choice=(battingorballing-{comps_choice}).pop()
            
else:
    sys.exit('Invalid input')
runs=0
runs2=0
goal=0

if choice =='batting':
    batting(runs,runs2,goal)
elif choice =='balling':
    balling(runs,runs2,goal)
else:
    sys.exit('Invalid')

