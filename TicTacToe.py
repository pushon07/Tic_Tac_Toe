# Tic Tac Toe

import random
import time
from six.moves import input

def drawBoard(board, first_line=True):
	# This function prints out the board that it was passed.

	# "board" is a list of 10 strings representing the board (ignore index 0)
	if first_line == True:
		print("\nThe current state of the board is:")
	print("   |   |")
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print("   |   |")
	print('-----------')
	print("   |   |")
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print("   |   |")
	print('-----------')
	print("   |   |")
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print("   |   |")

def inputPlayerLetter(player_name):
	# Lets the player type which letter they want to be.
	letter = ''
	while not (letter == 'X' or letter == 'O'):
		print('\n%s, which sign you wanna use? X or O?' % player_name)
		letter = input().upper()

	#The first element in the list is the player's letter, and the second one is the computer's letter
	if letter == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']

def whoGoesFirst():
	# Randomly choose the player who goes first.
	if random.randint(0, 1) == 0:
		return 'computer'
	else:
		return 'player'

def playAgain():
	print('\nDo you want to play again? (yes or no)')
	return not(input().lower().startswith('n'))

def makeMove(board, letter, move):
	board[move] = letter

def isWinner(bo, le):
	isWinner = ((bo[7] == le and bo[8] == le and bo[9] == le)\
			or (bo[4] == le and bo[5] == le and bo[6] == le)\
			or (bo[1] == le and bo[2] == le and bo[3] == le)\
			or (bo[7] == le and bo[4] == le and bo[1] == le)\
			or (bo[8] == le and bo[5] == le and bo[2] == le)\
			or (bo[9] == le and bo[6] == le and bo[3] == le)\
			or (bo[7] == le and bo[5] == le and bo[3] == le)\
			or (bo[9] == le and bo[5] == le and bo[1] == le))
	return isWinner

def getBoardCopy(board):
	dupeBoard = []
	for i in board:
		dupeBoard.append(i)

	return dupeBoard

def isSpaceFree(board, move):
	# Return true if the passed move is free on the passed board.
	return board[move] == ' '

def getPlayerMove(board, playerLetter, player_name):
	# Given a board and the computer's letter, determine where to move and return that move.
	# Let the player type in their move.
	move = ' '
	while ((move not in '1 2 3 4 5 6 7 8 9'.split()) or not(isSpaceFree(board, int(move)))):
		print('\n%s, what is your next move? (1-9) | You are using "%s"' % (player_name, playerLetter))
		move = input()
	return int(move)

def chooseRandomMoveFromList(board, movesList):
	# Returns a valid move from the passed list on the passed board.
	possibleMoves = []
	for i in movesList:
		if isSpaceFree(board, i):
			possibleMoves.append(i)

	if len(possibleMoves) != 0:
		return random.choice(possibleMoves)
	else:
		return None

def getComputerMove(board, computerLetter, starter, player_moves, game_level):
	# Given a board and the computer's letter, determine where to move and return that move.
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	# Here is our algorithm for our Tic Tac Toe AI:
	# First, check if we can win in the next move
	for i in range(1, 10):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, computerLetter, i)
			if isWinner(copy, computerLetter):
				return i

	# Check if the player could win on their next move, and block them.
	for i in range(1, 10):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, playerLetter, i)
			if isWinner(copy, playerLetter):
				return i

	if ((game_level == 1) or ((game_level == 2) and (starter == 'computer')) or ((starter == 'computer') and (len(player_moves) == 1) and (player_moves[0] in [1, 3, 7, 9, 5]))\
		 or ((starter == 'computer') and (len(player_moves) != 1)) or ((starter == 'player') and (player_moves[0] == 5))):
		# Try to take one of the corners, if they are free.
		move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
		if move != None:
			return move
		if isSpaceFree(board, 5):
			return 5
		# Move on one of the sides.
		return chooseRandomMoveFromList(board, [2, 4, 6, 8])

	elif (((game_level == 2) and (starter == 'player')) or ((game_level == 3) and (starter == 'player') and (player_moves[0] in [1, 3, 7, 9]))):
		if isSpaceFree(board, 5):	#first try to take the center
			return 5
		elif ((len(player_moves) == 2) and (player_moves[1] in [2, 4, 6, 8])):
			if player_moves[1] == 2:
				return chooseRandomMoveFromList(board, [1, 3])
			elif player_moves[1] == 4:
				return chooseRandomMoveFromList(board, [1, 7])
			elif player_moves[1] == 6:
				return chooseRandomMoveFromList(board, [3, 9])
			elif player_moves[1] == 8:
				return chooseRandomMoveFromList(board, [7, 9])
		
		else:
			move = chooseRandomMoveFromList(board, [2, 4, 6, 8])
			if move != None:
				return move
			# Move on one of the sides.
			return chooseRandomMoveFromList(board, [1, 3, 7, 9])

	elif ((game_level == 3) and (player_moves[0] in [2, 4, 6, 8])):
		if ((len(player_moves) == 1) and (starter == 'player')):
			if player_moves[0] == 2:
				return chooseRandomMoveFromList(board, [1, 3])
			elif player_moves[0] == 4:
				return chooseRandomMoveFromList(board, [1, 7])
			elif player_moves[0] == 6:
				return chooseRandomMoveFromList(board, [3, 9])
			elif player_moves[0] == 8:
				return chooseRandomMoveFromList(board, [7, 9])

		elif ((len(player_moves) == 1) and (starter == 'computer')):
			return 5
			# computer_first_move = board.index(computerLetter)	#to get the first move of computer
			# rand_move = random.choice([1, 2])
			# if rand_move == 1:	#two stratagies to win if computer starts and player's first move is in [2, 4, 6, 8]
			# 	return 5		#1st: take the center in the second move
			# elif rand_move == 2:#2nd: take the corner for making direct game
			# 	if computer_first_move in [1, 3] and player_moves[0] in [4, 6]:
			# 		return chooseRandomMoveFromList(board, [1, 3])
			# 	elif computer_first_move in [1, 7] and player_moves[0] in [2, 8]:
			# 		return chooseRandomMoveFromList(board, [1, 7])
			# 	elif computer_first_move in [3, 9] and player_moves[0] in [2, 8]:
			# 		return chooseRandomMoveFromList(board, [3, 9])
			# 	elif computer_first_move in [7, 9] and player_moves[0] in [4, 6]:
			# 		return chooseRandomMoveFromList(board, [7, 9])
			# 	else:
			# 		return 5

		elif (len(player_moves) > 1):
			if isSpaceFree(board, 5):	#first try to take the center
				return 5
			move = chooseRandomMoveFromList(board, [2, 4, 6, 8])
			if move != None:
				return move
			# Move on one of the sides.
			return chooseRandomMoveFromList(board, [1, 3, 7, 9])

def isBoardFull(board):
	# Return True if every space on the board has been taken. Otherwise return False.
	for i in range(1, 10):
		if isSpaceFree(board, i):
			return False	
	return True

def run_game(playerLetter, computerLetter, player_name, game_level=2, player2_name='Computer'):
	game_level = game_level
	num_game = 0
	results = {(player_name + ' Wins'):0, (player2_name + ' Wins'):0, 'Tie':0}

	while True:
		num_game += 1
		# Reset the board
		theBoard = [' '] * 10

		starter = whoGoesFirst()
		turn = starter
		player_moves = []
		if turn == 'player':
			print("\n%s, you will start the game." % player_name)
			drawBoard(theBoard)
		else:	
			print('\n' + player2_name + ' will go first.')

		gameIsPlaying = True

		while gameIsPlaying:
			if turn == 'player':
				#Player's turn
				move = getPlayerMove(theBoard, playerLetter, player_name)
				player_moves.append(move)
				makeMove(theBoard, playerLetter, move)
				drawBoard(theBoard)

				if isWinner(theBoard, playerLetter):
					print('\nHooray, %s! You have won the game!! :)' % player_name)
					results[player_name + ' Wins'] += 1
					gameIsPlaying = False

				else:
					if isBoardFull(theBoard):
						print('\nThe game is a tie!')
						results['Tie'] += 1
						break
					else:
						turn = 'computer'


			else:
				#Computer or player2's turn
				if game_mode == '1':
					move = getComputerMove(theBoard, computerLetter, starter, player_moves, game_level)
					makeMove(theBoard, computerLetter, move)
					time.sleep(1)
					drawBoard(theBoard)
				elif game_mode == '2':
					move = getPlayerMove(theBoard, computerLetter, player2_name)
					makeMove(theBoard, computerLetter, move)
					drawBoard(theBoard)

				if isWinner(theBoard, computerLetter):
					print('\n%s has beaten you! You lose, %s.' % (player2_name, player_name))
					results[player2_name + ' Wins'] += 1
					gameIsPlaying = False
				else:
					if isBoardFull(theBoard):
						print('\nThe game is a tie!')
						results['Tie'] += 1
						break
					else:
						turn = 'player'

		time.sleep(1)
		if not playAgain():
			break

	return results

def main():
	print('Welcome to Tic Tac Toe!')
	player_name = input("\nWhat's your name? ->")

	print("Please select the game mode - single or dual mode?")
	print("In single mode you will play with the computer.")
	time.sleep(1)
	print("While in dual mode, you will play with another player.")
	global game_mode
	game_mode = ''
	while not((game_mode == '1') or (game_mode == '2')):
		game_mode = input("\nEnter '1' for single mode and '2' for dual mode ->")

	if (game_mode == '2'):
		player2_name = input("%s, please enter your opponent's name ->" % (player_name)) or 'Hermaione'
		player2_name = player2_name[0].upper() + player2_name[1:]

	if game_mode == '1':
		game_level = input("\nSelect Game Difficulty: Easy=1; Normal=2; Hard=3 ->")
		while game_level not in ['1', '2', '3']:
			game_level = input("\nPlease Enter 1, 2, or 3 ->")
		game_level = int(game_level)		

	board_keys = "0 1 2 3 4 5 6 7 8 9".split()
	print("\nThanks for playing. %s, let's see the key for each board move/position:" % player_name)
	drawBoard(board_keys, first_line=False)
	playerLetter, computerLetter = inputPlayerLetter(player_name)
	time.sleep(1)

	if game_mode == '1':
		result = run_game(playerLetter, computerLetter, player_name, game_level)
	elif game_mode == '2':
		result = run_game(playerLetter, computerLetter, player_name, 2, player2_name)

	print ("\nResult: %s\n" % result)

if __name__ == '__main__':

	main()