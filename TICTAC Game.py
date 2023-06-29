import random

def display_board(board):
    
    print('\n'*50)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
   

test_board = ['#','X','O','X','O','X','O','X','O','X']


# player marker input

def placemarker(board, position, marker):
    board[position] = marker


#random choose first

def randomchoice():
    if random.randint(0, 1) == 0:
        return 'player 1'
    else:
        return 'player 2'


#position

def playerposition():

    position = 0

    while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        position = input(' Please input a number between 1-9: ')

        if position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print('Please enter a valid number!')
            
    return int(position)


#place marker

def choosemarker():
    marker= ''

    while not (marker == 'X' or marker == 'O'):
        marker = input("Please choose a letter X or O: ")

    if marker == 'X':
        return ( 'X', 'O')
    else:
        return ( 'O', 'X')
                         
#Win check

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

#space check
    
def spacecheck(board, position):
    return board[position]== '-'

#draw check 
    
def drawcheck(board):
    for i in range(1,10):
        if spacecheck(board, i):
            return False
    return True
        
   
#replay

def replay():

    return input('Do you want to play again? Enter Y or N: ').lower().startswith('y') # you need something that return true in order to continue the while true loop!!

print('Welcome to Tic Tac Toe!')

#game play

while True: # this will execute all the below code until you break out on the same level indent ( the other breaks will quit the game on loop)

    board = ['-','-','-','-','-','-','-','-','-','-']
    turn = randomchoice()
    player1, player2 =  choosemarker()



    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Y or N.')
        
    if play_game == 'y' or 'Y':
        gameon = True
    else:
        gameon = False


    while gameon:
        if turn == 'player 1' :
            position = playerposition()
            if spacecheck(board, position):
                placemarker(board, position, player1)
                display_board(board)

                if win_check(board,player1):
                    print(" Congratulations !, Player 1 won!")
                    gameon = False  

                else:
                    if drawcheck(board):
                        print("OOPS its a draw")
                        gameon = False
                        break
                    else:
                        turn = 'player 2'  
            else:
                print("oops that space is taken")
         
           

        else:

            if turn == 'player 2' :
                position = playerposition()
                if spacecheck(board, position):
                    placemarker(board, position, player2)
                    display_board(board)

                    if win_check(board,player2):
                        print(" Congratulations, Player 2 won!")
                        gameon = False
                                        
                    else:
                        if drawcheck(board):
                            print("OOPS its a draw")
                            gameon = False
                            break
                         
                        else:
                            turn = 'player 1'
                else:
                    print("oops that space is taken")

    if not replay():
        break
           

    

    

    











