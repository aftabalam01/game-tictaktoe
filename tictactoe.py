# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from IPython.display import clear_output
import random

BOARD_INIT = [' ']*10

def player_name():
    name1 = input("Player 1 Name: ")
    name2 = input("Player 2 Name: ")
    return (name1,name2)
player1_name,player2_name = player_name()
def display_board(board):
        #print('-|-|-')
        clear_output()
        print(board[7] + '|' + board[8] + '|'+ board[9])
        print('-|-|-')
        print(board[4] + "|" + board[5] + "|" + board[6])
        print('-|-|-')
        print(board[1] + "|" + board[2] + "|" +board[3])
       
def player_input():
    # ask for player 1 input
    marker_set = {'X','O'}
    marker_player1 = ' '
    while  marker_player1 not in marker_set:
        marker_player1 = input(player1_name+' please select X or O : ')
        
    marker_set1 = {marker_player1}  
    
    marker_list = list(marker_set.difference(marker_set1))
    marker_player2 = marker_list[0]
    
    print(player1_name+ " has selected "+ marker_player1 + "\n "+ player2_name + " has selected " + marker_player2 )
    return (marker_player1, marker_player2)

def place_marker(board,marker,position):
    board[position] = marker
    display_board(board)

def win_check(board, mark):
    #check if any of the rows has same mark
    for i in (1,4,7):            
            if board[i]==board[i+1]==board[i+2]==mark :
                return  True
    
    # check if any of the collumn has same mark
    for i in (1,2,3):            
            if board[i]==board[i+3]==board[i+6]==mark :
                return True
    
    # check if any of diagonal has same mark 
   
    if (board[1]==board[5]==board[9]==mark or board[3]==board[5]==board[7]==mark):
        return True
    return False

def choose_first():
    flip_coin = random.randint(0,1)
    if flip_coin == '0':
        return player1_name
    else :
        return player2_name
 
def space_check(board, position):
    return board[position]==' '
def board_full_check(board):
    for i in range(1,10):
        if space_check(board,i) :
            return False
    return True
def player_choice(turn,board)  :
    position = 0
    while position not in range(1,10) or not space_check(board, position):
        try:
            position = int( input(turn+' Choose a position: (1-9): '))
        except ValueError :
            continue
    return position
def replay() :
    choice = input("Do you want play again? Enter Yes or No")
    return choice[0].lower == 'y'
def play_game():
    choice = input("Ready to play? Enter Yes or No")
    return choice[0].lower == 'y'

def play_tictactoe():
    print("Welcome to tictactoe")
    while True :
        # initiate the board
        the_board = [' ']*10
        player1_marker,player2_marker = player_input()
        display_board(the_board)
        #choose player
        turn = choose_first()
        print(turn + " will go first")
        
        if play_game() :
            game_on = True
        else:
           game_on = False 
        
        while game_on :
           if turn == player1_name :
               #show the board
               display_board(the_board)
               
               # choose position
               position = player_choice(turn,the_board)
               
               # place the marker
               place_marker(the_board,player1_marker,position)
               
               # chekc if win
               if  win_check(the_board,player1_marker):
                 
                  display_board(the_board)
                  print("Congrats " + player1_name+" Won !!")
                  game_on = False
               
               # check if board is full
               else:
                       if board_full_check(the_board):
                           
                           display_board(the_board)
                           print("Game is tie!!")
                           game_on = False
                       else:
                           turn = player2_name
        
           else:
               #show the board
               display_board(the_board)
               
               # choose position
               position = player_choice(turn,the_board)
               
               # place the marker
               place_marker(the_board,player2_marker,position)
               
               # chekc if win
               if  win_check(the_board,player2_marker):
                  display_board(the_board)
                  print("Congrats " + player2_name+" Won !!")
                 
                  game_on = False
               
               # check if board is full
               else:
                   if board_full_check(the_board):
                       
                       display_board(the_board)
                       print("Game is tie!!")
                       game_on = False
                   else:
                       turn = player1_name
        if not replay():
            break
        
def test():
    testboard= ['#','X','O','X','O','X','O','X','O','X']
    display_board(testboard)
    place_marker(testboard,"X",2)
    mark = 'X'
    if win_check(testboard,mark):
        print (mark + " has won")
    



if __name__ == '__main__':
  play_tictactoe()
