pets = [
	{'name': 'rex', 'animal': 'dog', 'owner': 'martha'},
	{'name': 'cleo', 'animal': 'cockatiel', 'owner': 'arina'},
	{'name': 'me-mow', 'animal': 'cat', 'owner': 'me-mow'},
	]

for pet in pets:
	print(f"{pet['name'].title()} is a {pet['animal']} owned by {pet['owner'].title()}.")