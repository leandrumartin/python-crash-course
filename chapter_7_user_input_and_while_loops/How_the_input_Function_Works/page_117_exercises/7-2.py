party_size = int(input("How many people are there? "))

if party_size > 8:
	print("I'm sorry, but you'll have to wait for a table.")
else:
	print(f"Your table for {party_size} is ready.")