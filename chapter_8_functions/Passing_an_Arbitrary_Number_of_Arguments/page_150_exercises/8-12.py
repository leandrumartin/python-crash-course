def make_sandwich(bread, *fillings):
	print(f"\nMaking a sandwich with {bread} bread and the following items inside:")
	for filling in fillings:
		print(f"	- {filling}")

make_sandwich('white', 'peanut butter', 'jelly')
make_sandwich('Italian herbs and cheese', 'salami', 'provolone', 'lettuce', 'tomatoes', 'spinach', 'honey mustard')
make_sandwich('rye', 'toast')