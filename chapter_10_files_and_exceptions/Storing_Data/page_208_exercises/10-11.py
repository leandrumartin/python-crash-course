import json

filename = 'favorite_number.json'

fav = input("What is your favorite number? ")
try:
	fav = int(fav)
except ValueError:
	fav = float(fav)

with open(filename, 'w') as f:
	json.dump(fav, f)