favorite_numbers = {
	'atticus': [3, 18],
	'bob': [99, 4, 22],
	'caitlyn': [7],
	'deborah': [2, 100],
	'earl': [8, 13],
	}

for person, numbers in favorite_numbers.items():
	print(f"{person.title()}'s favorite numbers are:")
	for number in numbers:
		print(f"\t{number}")

# This shows that using the for function in this way makes it possible to extract the keys of a dictionary.