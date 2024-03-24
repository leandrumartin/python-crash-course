def program():
	exercise = input('Which exercise would you like to run? (type a number 2.3-2.7) ')

	if exercise == '2.3':
		name = "eric"
		print(f"Hello {name.title()}, would you like to learn some Python today?")

	elif exercise == '2.4':
		print ('See name.py.')

	elif exercise == '2.5':
		name = 'Benjamin Franklin'
		quote = 'Early to bed and early to rise makes a man healthy, wealthy, and wise.'
		print(f'{name} once said, "{quote}"')

	elif exercise == '2.6':
		famous_person = 'Benjamin Franklin'
		quote = 'Fish and visitors stink in three days.'
		message = f'{famous_person} once said, "{quote}"'
		print(message)

	elif exercise == '2.7':
		name = " bob "
		print(f'{name}.')
		print(f'{name.lstrip()}.')
		print(f'{name.rstrip()}.')
		print(f'{name.strip()}.')
		
program()