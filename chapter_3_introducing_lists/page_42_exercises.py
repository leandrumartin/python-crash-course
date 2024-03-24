def program():
	exercise = input('Which exercise would you like to run? (type a number 3.4-3.7) ')

	if exercise == '3.4':
		invitees = ['your mom', 'martin luther king', 'obama']
		for invitee in invitees:
			print(f'Hello, {invitee.title()}, would you like to come to dinner with me?')

	elif exercise == '3.5':
		invitees = ['your mom', 'martin luther king', 'obama']
		for invitee in invitees:
			print(f'Hello, {invitee.title()}, would you like to come to dinner with me?')
		popped_invitee = invitees.pop(0)
		print(f"Unfortunately, {popped_invitee.title()} can't make it!")
		for invitee in invitees:
			print(f'Hello, {invitee.title()}, would you like to come to dinner with me?')

	elif exercise == '3.6':
		invitees = ['your mom', 'martin luther king', 'obama']
		for invitee in invitees:
			print(f'Hello, {invitee.title()}, would you like to come to dinner with me?')
		popped_invitee = invitees.pop(0)
		print(f"Unfortunately, {popped_invitee.title()} can't make it!")
		for invitee in invitees:
			print(f'Hello, {invitee.title()}, would you like to come to dinner with me?')
		print('Wait, I just found a bigger table!')
		invitees.insert(0, 'your dad')
		invitees.insert(len(invitees) // 2, 'mario')
		invitees.append('bowser')
		for invitee in invitees:
			print(f'Hello, {invitee.title()}, would you like to come to dinner with me?')
	
	elif exercise == '3.7':
		invitees = ['your mom', 'martin luther king', 'obama']
		for invitee in invitees:
			print(f'Hello, {invitee.title()}, would you like to come to dinner with me?')
		popped_invitee = invitees.pop(0)
		print(f"Unfortunately, {popped_invitee.title()} can't make it!")
		for invitee in invitees:
			print(f'Hello, {invitee.title()}, would you like to come to dinner with me?')
		print('Wait, I just found a bigger table!')
		invitees.insert(0, 'your dad')
		invitees.insert(len(invitees) // 2, 'mario')
		invitees.append('bowser')
		for invitee in invitees:
			print(f'Hello, {invitee.title()}, would you like to come to dinner with me?')
		print('Oh no! I can now only invite two people over for dinner!')
		for uninvited_number in range(0, len(invitees)-2):
			uninvited_name = invitees.pop(0)
			print(f"I'm sorry, {uninvited_name.title()}, but you can't come to dinner!")
		for still_invited in invitees:
			print(f"{still_invited.title()}, you're still invited.")
		del invitees[0]
		del invitees[0]
		print(invitees)

program()