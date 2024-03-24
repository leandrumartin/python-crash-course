favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")

print('\n')

for name in favorite_languages.keys():
	print(name.title())

# You can achieve the above result (printing the keys) by doing this too:
print('\n')

for name in favorite_languages:
	print(name.title())

# You can choose to include the keys() method if it makes your code easier to read.

print('\n')

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(f"Hi {name.title()}.")

	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

# Looping through keys in a particular order

for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")

# Looping through all values

print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

# Using set() to make sure there are no repeats

print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())

# How to make a set. Note that like dictionaries, it's in braces, but is different! A set has no key-value pairs. Sets remove repeat values.
languages = {'python', 'ruby', 'python', 'c'}
print('\n')
print(languages)