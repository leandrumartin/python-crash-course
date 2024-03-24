def program():
	exercise = input('Which exercise would you like to run? (type a number 2.8-2.9) ')
	
	if exercise == '2.8':
		print(5 + 3)
		print(24 / 3)
		print(2 ** 3)
		print(4 * 2)
		print(10 - 2)
	
	elif exercise == '2.9':
		favorite_number = 7_777_777
		print(f'My favorite number is {favorite_number}!')

program()