favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

people = ['jen', 'sarah', 'edward', 'bob', 'joe', 'phil', 'emma', 'stewart']

for person in people:
	if person in favorite_languages.keys():
		print(f"{person.title()}, thank you for taking the poll!")
	else:
		print(f"{person.title()}, please take my poll on what your favorite language is.")