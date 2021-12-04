board_slots = {'7': ' ', '8': ' ', '9': ' ',
               '4': ' ', '5': ' ', '6': ' ',
               '1': ' ', '2': ' ', '3': ' '}


def board_display(board):
    print(f'{board["7"]}' + '|' + f'{board["8"]}' + '|' + f'{board["9"]}')
    print('-+-+-')
    print(f'{board["4"]}' + '|' + f'{board["5"]}' + '|' + f'{board["6"]}')
    print('-+-+-')
    print(f'{board["1"]}' + '|' + f'{board["2"]}' + '|' + f'{board["3"]}')


def the_game():
    turn = 'X'
    count = 0

    for integer in range(10):
        board_display(board_slots)

        move = input()

        if board_slots[move] == ' ':
            board_slots[move] = turn
            count += 1
        else:
            print('That spot is taken. Pick a different one.')
            continue

        if count >= 5:
            if board_slots['7'] == board_slots['8'] == board_slots['9']:
                print('Game Over.')
                print(f'Player {turn} wins.')
                break
            elif board_slots['4'] == board_slots['5'] == board_slots['6']:
                print('Game Over.')
                print(f'Player {turn} wins.')
                break
            elif board_slots['1'] == board_slots['2'] == board_slots['3']:
                print('Game Over.')
                print(f'Player {turn} wins.')
                break
            elif board_slots['1'] == board_slots['4'] == board_slots['9']:
                print('Game Over.')
                print(f'Player {turn} wins.')
                break
            elif board_slots['2'] == board_slots['5'] == board_slots['8']:
                print('Game Over.')
                print(f'Player {turn} wins.')
                break
            elif board_slots['3'] == board_slots['6'] == board_slots['9']:
                print('Game Over.')
                print(f'Player {turn} wins.')
                break
            elif board_slots['1'] == board_slots['5'] == board_slots['9']:
                print('Game Over.')
                print(f'Player {turn} wins.')
                break
            elif board_slots['3'] == board_slots['5'] == board_slots['7']:
                print('Game Over.')
                print(f'Player {turn} wins.')
                break
        if count == 9:
            print('Game Over.')
            print("It's a tie.")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


the_game()