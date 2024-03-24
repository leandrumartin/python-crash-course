import json

def get_stored_number():
	"""Get stored favorite number if available."""
	filename = 'favorite_number.json'
	try:
		with open(filename) as f:
			return json.load(f)
	except FileNotFoundError:
		return None

def get_new_number():
	"""Ask for and return a new favorite number."""
	fav = input("What is your favorite number? ")
	try:
		fav = int(fav)
	except ValueError:
		fav = float(fav)
	return fav

def get_favorite_number():
	"""Ask for or retrieve the user's favorite number."""
	filename = 'favorite_number.json'
	fav = get_stored_number()
	if fav:
		print(f"I know your favorite number! It's {fav}!")
	else:
		fav = get_new_number()
		with open(filename, 'w') as f:
			json.dump(fav, f)

get_favorite_number()