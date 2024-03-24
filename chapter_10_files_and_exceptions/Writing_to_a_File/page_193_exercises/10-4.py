filename = 'guest_book.txt'

active = True
while active:
	name = input("What is your name? (type q to quit) ")
	if name == 'q':
		active = False
	else:
		with open(filename, 'a') as file_object:
			file_object.write(f'{name}\n')