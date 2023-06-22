#Contraints:
# - Add two users
# - Show the format of Tic Tac Toe after every turn
# - input from the user alternatively
# - Comp[are for results]
# - Declare the winner

#HINT:
# ->change turn after every iterations (X or O)
# ->comparison will be only be possible after 5 turns
# ->match will be a tie after the 9th or last turn is over

#Advice : 
# ->create functions for cocurrent process
# ->Organise your code and add comments


#for  i in  range(10):
#turn = "X"
#take the input from the user
#check if it is empty
# i its not empty the take the again
#If  turn =="X"
#     turn=="O"
#    else:
#       turn ="O"
#def check():
#if board[1]==board[2]==board[3]!= ' ':
#       print(f"{turn} wins")
#         break
#     if i==9
#      print("Its a tie")

board={
    1:' ',2:' ',3:' ',
    4:' ',5:' ',6:' ',
    7:' ',8:' ',9:' ',
}

def iteration(turn,player):
    print_board()
    print('Turn : ',turn)
    print('Player : ',player)
    print('Enter row : ')
    print('Enter col : ')
    row=int(input())
    col=int(input())
    if board[row]==' ':
        board[row]=player
        print('Player : ',player)
    elif board[col]==' ':
        board[col]=player
        print('Player : ',player)
    elif board[row]==' ':
        board[row]=turn
        print('Turn : ',turn)
    elif board[col]==' ':
        board[col]=turn
        print('Turn : ',turn)
    else:
        print('Match : ',player)
        print_board()
        return True
    return False
def winner(player):
    if board[1]==board[2]==board[3]!= ' ':
        return board[1]
    elif board[4]==board[5]==board[6]!= ' ':
        return board[4]
    elif board[7]==board[8]==board[9]!= ' ':
        return board[7]
    elif board[1]==board[4]==board[7]!= ' ':
        return board[1]
    elif board[2]==board[5]==board[8]!= ' ':
        return board[2]
    elif board[3]==board[6]==board[9]!= ' ':
        return board[3]
    elif board[1]==board[5]==board[9]!= ' ':
        return board[1]
    elif board[3]==board[5]==board[7]!= ' ':
        return board[3]
    else:
        return ' '
def end_game(player):
    if winner(player)!=' ':
        print('Winner : ',winner(player))
        print('Match : ',player)
        return True
    else:
        return False
def print_board():
    print(board[1]+'|'+board[2]+'|'+board[3])
    print('-+-+-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-+-+-')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-+-+-')
