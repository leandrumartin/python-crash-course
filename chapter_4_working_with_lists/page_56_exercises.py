answer = input('Which exercise would you like to run? Choose a number from 4.1-4.2.')

if answer == '4.1':
	pizzas = ['pepperoni', 'sausage', 'mushroom']
	for pizza in pizzas:
		print(pizza)
	print('\n')
	for pizza in pizzas:
		print(f'I like {pizza.lower()} pizza.')
	print('\n')
	print('I REALLY like pizza!')

elif answer == '4.2':
	reptiles = ['snake', 'lizard', 'turtle']
	for reptile in reptiles:
		print(reptile)
	print('\n')
	for reptile in reptiles:
		print(f'A {reptile.lower()} would make a great pet.')
	print('\n')
	print('Any of these reptiles would make a great pet!')