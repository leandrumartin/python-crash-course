favorite_places = {
	'jenna': ['rome', 'new york'],
	'bob': ['san fransisco', 'murdale walmart', 'texas'],
	'dave': ['where the heart is'],
	}

for name, places in favorite_places.items():
	print(f"{name.title()}'s favorite places are:")
	for place in places:
		print(f"\t{place.title()}")