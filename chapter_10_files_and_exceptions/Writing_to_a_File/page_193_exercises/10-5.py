filename = 'reasons.txt'

active = True
while active:
	reason = input('Why do you like programming? (enter "quit" to quit) ')
	if reason == 'quit':
		active = False
	else:
		with open(filename, 'a') as file_object:
			file_object.write(f'{reason}\n')