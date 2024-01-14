def Result(user1moves, user2moves):
	if set(user1moves).issuperset({"a1","a2","a3"}):
		return "User 1 won."
	elif set(user1moves).issuperset({"b1","b2","b3"}):
		return "User 1 won."
	elif set(user1moves).issuperset({"c1","c2","c3"}):
		return "User 1 won."
	elif set(user1moves).issuperset({"a1","b1","c1"}):
		return "User 1 won."
	elif set(user1moves).issuperset({"a2","b2","c2"}):
		return "User 1 won."
	elif set(user1moves).issuperset({"a3","b3","c3"}):
		return "User 1 won."
	elif set(user1moves).issuperset({"a1","b2","c3"}):
		return "User 1 won."
	elif set(user1moves).issuperset({"c1", "b2", "a3"}):
		return "User 1 won."
	
	if set(user2moves).issuperset({"a1","a2","a3"}):
		return "User 2 won."
	elif set(user2moves).issuperset({"b1","b2","b3"}):
		return "User 2 won."
	elif set(user2moves).issuperset({"c1","c2","c3"}):
		return "User 2 won."
	elif set(user2moves).issuperset({"a1","b1","c1"}):
		return "User 2 won."
	elif set(user2moves).issuperset({"a2","b2","c2"}):
		return "User 2 won."
	elif set(user2moves).issuperset({"a3","b3","c3"}):
		return "User 2 won."
	elif set(user2moves).issuperset({"a1","b2","c3"}):
		return "User 2 won."
	elif set(user2moves).issuperset({"c1", "b2", "a3"}):
		return "User 2 won."

def OneOnOne(user1, user2):
	board = '''
   a     b     c
      |     |    
1  a1 |  b1 |  c1  
 _____|_____|_____
      |     |    
2  a2 |  b2 |  c2  
 _____|_____|_____
      |     |    
3  a3 |  b3 |  c3  
      |     |    
	'''  
	print(board)
	import random
	coordinates = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
	user1_set = set()
	user2_set = set()
	print(f"{user1} is playing as X.")
	print(f"{user2} is playing as O.")
	for i in range(5):
		if user1 != "Computer":
			user1_move = input(f"{user1}, enter coordinate where you want to place your piece: ")
			user1_set.add(user1_move)
			board = board.replace(user1_move, "X ")
			coordinates.remove(user1_move)
			print(board)
		else:
			computer_move = random.choice(coordinates)
			user1_set.add(computer_move)
			coordinates.remove(computer_move)
			board = board.replace(computer_move, "X ")
			print("Computer chose", computer_move)
			print(board)
		if coordinates != []:
			if user2 != "Computer":
				user2_move = input(f"{user2}, enter coordinate where you want to place your piece: ")
				user2_set.add(user2_move)
				coordinates.remove(user2_move)
				board = board.replace(user2_move, "O ")
				print(board)
			else:
				computer_move = random.choice(coordinates)
				user2_set.add(computer_move)
				coordinates.remove(computer_move)
				board = board.replace(computer_move, "O ")
				print("Computer chose", computer_move)
				print(board)
		if Result(user1_set, user2_set) == "User 1 won.":
			print(f"{user1} won.")
			break
		elif Result(user1_set, user2_set) == "User 2 won.":
			print(f"{user2} won.")
			break
	else:
		print("Game drawn.")

while True:
	try:
		import random
		mode = int(input("""Do you want to play against -
Computer (Press 1)
or
A friend (Press 2)
>>> """))
		if mode == 1:
			user = input("Enter your name: ")
			players = [user, "Computer"]
			first_player = players[random.randint(0, 1)]
			players.remove(first_player)
			second_player = players[0]
			OneOnOne(first_player, second_player)
		elif mode == 2:
			user = input("Enter first user's name: ")
			user_ = input("Enter second user's name: ")
			players = [user, user_]
			first_player = players[random.randint(0, 1)]
			players.remove(first_player)
			second_player = players[0]
			OneOnOne(first_player, second_player)
		cont = input("Press Q to quit and anything else to continue: ").lower()
		if cont == 'q':
			break
	except:
		print("Invalid input.")