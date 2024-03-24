people = [
	{'first_name': 'jeff', 'last_name': 'robinson', 'age': 18, 'city': 'carbondale'},
	{'first_name': 'martha', 'last_name': 'johnson', 'age': 19, 'city': 'marion'},
	{'first_name': 'john', 'last_name': 'jefferson', 'age': 17, 'city': 'murphysboro'},
	]

for person in people:
	print(f"My friend {person['first_name'].title()} {person['last_name'].title()} is {person['age']} years old and lives in {person['city'].title()}.")