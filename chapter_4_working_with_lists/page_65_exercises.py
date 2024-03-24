answer = input('Which exercise would you like to run? Choose a number from 4.10 to 4.12.')

if answer == 4.10:
	players = ['charles', 'martina', 'michael', 'florence', 'eli']

	print('The first three items in the list are:')
	print(players[:3])

	print('Three items from the middle of the list are:')
	print(players[1:4])

	print('The last three items are:')
	print(players[2:])

elif answer == 4.11:
	pizzas = ['pepperoni', 'sausage', 'mushroom']
	friend_pizzas = pizzas[:]

	pizzas.append('Dominic from Mod Pizza')
	friend_pizzas.append('pineapple')

	print('My favorite pizzas are:')
	print(pizzas)

	print("My friend's favorite pizzas are:")
	print(friend_pizzas)

elif answer == 4.12:
	foods = ['pizza', 'falafel', 'carrot cake']
	for food in foods:
		print(food)