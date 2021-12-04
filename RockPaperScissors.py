from random import randint


def victory():
    print('Congratulations!')
    print('You Win!')


def defeat():
    print('You Lose.')
    print('Try Again.')


play_options = ['rock', 'paper', 'scissors']

playing = True

while playing:
    player = input('Rock, Paper, or Scissors? ').lower()
    computer = play_options[randint(0, 2)]
    if player == computer:
        print('Tie.')
    elif player == 'rock':
        if computer == 'scissors':
            victory()
        else:
            defeat()
    elif player == 'paper':
        if computer == 'rock':
            victory()
        else:
            defeat()
    elif player == 'scissors':
        if computer == 'paper':
            victory()
        else:
            defeat()
    elif player == 'quit':
        print('Game Over.')
        break
    else:
        print("Sorry, I don't understand.")
        print('Please pick rock, paper, or scissors.')