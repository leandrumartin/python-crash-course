import json

filename = 'favorite_number.json'

try:
	with open(filename) as f:
		fav = json.load(f)
		print(f"I know your favorite number! It's {fav}!")
except FileNotFoundError:
	print("It looks like I don't know what your favorite number is.")