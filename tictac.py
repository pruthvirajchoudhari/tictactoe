import itertools

def win(current_game):

	def all_same(l):
		if l.count(l[0]) == len(l) and l[0] != 0:
			return True
		else:
			return False

	#Horizontal
	for row in game:
		print(row)
		if all_same(row):
			print(f"Player {row[0]} is the WINNER Horizontally")
			return True

	#Diagonal
	diags = []
	for col, row in enumerate(reversed(range(len(game)))):
		diags.append(game[row][col])
	if all_same(diags):
			print(f"Player {diags[0]} is the WINNER Diagonally(/)")
			return True

	diags = []
	for idx in range(len(game)):
		diags.append(game[idx][idx])
	if all_same(diags):
			print(f"Player {diags[0]} is the WINNER Diagonally(\\)")
			return True

	#Vertical
	for col in range(len(game)):
		vert = []

		for row in game:
			vert.append(row[col])	

		if all_same(vert):
			print(f"Player {row[0]} is the WINNER Vertically")
			return True

	return False


def game_board(game_map, player=0, row=0, col=0, just_display=False):
	try:
		if game_map[row][col] != 0:
			print("This position is occupied! choose another ")
			return game_map, False;
		print("   "+"  ".join([str(i) for i in range(len(game_map))]))
		if not just_display:
			game_map[row][col] = player
		for count, row in enumerate(game_map):
			print(count, row)
		return game_map, True

	except IndexError as e:
		print("make sure you input row/col as 0 1 or 2?", e)
		return game_map, False

	except Exception as e:
		print("Something went very wrong", e)
		return game_map,False



play = True
players = [1, 2]
while play:

	game_size = int(input("What size of tic tac toe do u want: "))
	game = [[0 for i in range(game_size)] for i in range(game_size)]
	game_won = False
	game, _ = game_board(game, just_display=True)
	player_choice = itertools.cycle([1, 2])
	while not game_won:
		current_player = next(player_choice)
		print(f"Current player: {current_player}")
		played = False

		while not played:
			column_choice = int(input("What column do u want to play?: "))
			row_choice = int(input("What row do u want to play?: "))
			game, played = game_board(game, current_player, row_choice, column_choice)


		if win(game):
			game_won = True
			again = input("Game is Over. Would u like to play again (y/n): ")
			if again.lower() == "y":
				print("Restarting...")
			elif  again.lower() == "n":
				print("BYE")
				play = False

			else:
				print("Not A Valid Answer")
				play = False