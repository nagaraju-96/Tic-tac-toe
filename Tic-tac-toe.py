import random  
import os

#function to print the board
def print_board(board):
	print('{} | {} | {} |'.format(board[0],board[1],board[2]))
	print('-----------')
	print('{} | {} | {} |'.format(board[3],board[4],board[5]))
	print('-----------')
	print('{} | {} | {} |'.format(board[6],board[7],board[8]))

#function to print the results
def result(player,win_status):
	if(win_status):
		if(player == player1):
			print(f'player1 "{player1}" Won the game')
		else:
			print(f'player2 "{player2}" Won the game')
	else:
		print('Game Drawn')

#function to fetch choose player symbol
def player_input():
	player1 = ''
	while(True):
		player1=input('Please Select your symbol from "O" or "X": ')
		if player1 in ['O','X','o','x']:
			break
	if (player1 in ['O','o']):
		return 'O','X'
	return 'X','O'

#function to checking weather player won or not
def win_check(board,player):
	return ((board[6] == player and board[7] == player and board[8] == player) or # across the top
    (board[3] == player and board[4] == player and board[5] == player) or # across the middle
    (board[0] == player and board[1] == player and board[2] == player) or # across the bottom
    (board[6] == player and board[3] == player and board[0] == player) or # down the middle
    (board[7] == player and board[4] == player and board[1] == player) or # down the middle
    (board[8] == player and board[5] == player and board[2] == player) or # down the right side
    (board[6] == player and board[4] == player and board[2] == player) or # diagonal
    (board[8] == player and board[4] == player and board[0] == player)) # diagonal

#Function to update the board
def place_marker(board,mark,player):
	board[mark]= player
	status =win_check(board,player)
	return board, status

#funcion about the main login
def start_play(board,player1, player2):
	choice = random.choice([player1,player2])
	print_board(board)
	count = 0
	while(count<9):
		while(True):
			try:
				mark = int(input(f'Choose position for {choice} :'))
			except:
				print('Please choose a valid number/position')
				continue
			else:
				break
		if mark in [0,1,2,3,4,5,6,7,8]:
			if mark in board:
				board,win_status=place_marker(board,mark,choice)
				os.system('cls')
				print_board(board)
				count=count+1
				if win_status:
					return choice,True
				if choice == 'X':
					choice = 'O'
				else:
					choice = 'X'
			else: 
				print("please choose empty position")
		else:
			print("please choose between 0 to 8")
	#print_board(board)
	return choice,False

#Driver of the program
player1=player2=''
board=[0,1,2,3,4,5,6,7,8]
player1,player2=player_input()
player,win_status=start_play(board,player1,player2)
result(player,win_status)
