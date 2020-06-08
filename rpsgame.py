import random
import sys

def text_to_int(user_in):
    if(user_in == 'rock' or user_in == 'Rock' or user_in == 'ROCK' or user_in == 'r' or user_in == 'R'):
        return 1
    elif(user_in == 'paper' or user_in == 'Paper' or user_in == 'PAPER' or user_in == 'p' or user_in == 'P'):
        return 2
    elif(user_in == 'scissors' or user_in == 'Scissors' or user_in == 'SCISSORS' or user_in == 's' or user_in == 'S'):
        return 3

def int_to_text(int_input):
    if(int_input == 1):
        return 'Rock'
    elif(int_input == 2):
        return 'Paper'
    elif(int_input == 3):
        return 'Scissors'

def winner(user_in, cpu_in):
    if(user_in == cpu_in):
        return 'Tie'
    elif((user_in == 1 and cpu_in == 3) or (user_in == 2 and cpu_in == 1) or (user_in == 3 and cpu_in == 2)):
        return 'Player'
    else:
        return 'CPU'

def text_format(user_in, cpu_in):
    try:
        print('Player chose: ' + int_to_text(user_in))
        print('CPU Chose:    ' + int_to_text(cpu_in))
        if(winner(user_in, cpu_in) == 'Tie'):
            print(winner(user_in, cpu_in))
        else:
            print('Winner is ' + winner(user_in, cpu_in))
    except TypeError:
        print('Unknown input, try again')

print('Rock, Paper, Scissors Game (press q to quit)')
while True:
    user_in = input('Player choice: ')
    if(user_in == 'q'):
        sys.exit()
    user_in_int = text_to_int(user_in)
    cpu_in = random.randint(1,3)
    text_format(user_in_int, cpu_in)