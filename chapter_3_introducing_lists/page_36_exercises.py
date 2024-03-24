def program():
	exercise = input('Which exercise would you like to run? (type a number 3.1-3.3) ')

	if exercise == '3.1':
		friends = ['Bob', 'Jim', 'Jane']
		for x in range(0,3):
			print(friends[x])

	elif exercise == '3.2':
		friends = ['bob', 'jim', 'jane']
		for x in range(0,3):
			print(f'My best friend is {friends[x].title()}')

	elif exercise == '3.3':
		teslas = ['model 3', 'cybertruck']
		buicks = ['encore', 'envision', 'enclave']
		toyotas = ['prius', 'corolla', 'camry']

		have_owned = ['enclave', 'corolla', 'camry']
		liked_teslas = ['model 3']

		vowels = ['a', 'e', 'i', 'o', 'u']

		for tesla in teslas:
			print('I would', end=' ')
			if not(tesla.lower() in liked_teslas):
				print('not', end=' ')
			print('like to own a', end='')
			if tesla[0] in vowels:
				print('n', end=' ')
			else:
				print('', end=' ')
			print(f'{tesla.title()}.')
		for buick in buicks:
			print('I have', end=' ')
			if not(buick.lower() in have_owned):
				print('not', end=' ')
			print('owned a', end='')
			if buick[0] in vowels:
				print('n', end=' ')
			else:
				print('', end=' ')
			print(f'{buick.title()}.')
		for toyota in toyotas:
			print('I have', end=' ')
			if not(toyota.lower() in have_owned):
				print('not', end=' ')
			print('owned a', end='')
			if toyota[0] in vowels:
				print('n', end=' ')
			else:
				print('', end=' ')
			print(f'{toyota.title()}.')

program()