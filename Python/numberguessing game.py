from random import randint
from urllib.parse import uses_relative
target = randint(1,20)
user_value = int(input("Guess number between 1-20:"))
game_over= False
guess = 1
while not game_over:
    if user_value == target:
        print('YOU WIN !!! & you guess the number in {} times'.format(guess)) 
        game_over = True  
    else: 
        if user_value > target:
            print('You are too HIGH!!!')
        else:
            print('You are too LOW!!!')
    guess+=1
    user_value = int(input('Guess Again:'))
