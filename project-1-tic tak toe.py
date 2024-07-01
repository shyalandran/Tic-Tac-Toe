import random

def display_board(board):
    print(board[1]+'|'+board[2]+"|"+board[3])
    print("-|-|-")
    print(board[4]+'|'+board[5]+"|"+board[6])
    print("-|-|-")
    print(board[7]+'|'+board[8]+"|"+board[9])

def player_input():
    choice = False

    while choice == False:
        player1 = input("player1:Please pick a marker 'X' or 'O' ")
        if player1 in ["x","o"]:
            choice = True
        else:
            print("can't understand pick either x or o")
    
    if player1 == "x":
        player2 = "o"
    else:
        player2 = "x"
        
    return player1,player2

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return((board[1] == board[2] == board[3] == mark)or(board[4] == board[5] == board[6] == mark)or(board[7] == board[8] == board[9] == mark)
           or(board[1] == board[4] == board[7] == mark)or(board[2] == board[5] == board[8] == mark)or(board[3] == board[6] == board[9] == mark)
           or(board[1] == board[5] == board[9] == mark)or(board[3] == board[5] == board[7] == mark))

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return "player 1"
    else:
        return "player 2"


def space_check(board, position):
    return board[position] == " "

def full_board_check(board):
    for num in range(1,10):
        if space_check(board,num):
            return False
        
    return True
        
def player_choice(board):
    potition = 0

    while potition not in range(1,10) or not space_check(board,potition):
        potition = int(input("choses position from 1 to 9"))

    return potition

def replay():
    choice = input("whant to play again?![y or n]")
    if choice == "y":
        return True
    else:
        return False
    

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


