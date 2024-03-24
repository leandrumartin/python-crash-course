pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

# This is how we can remove all instances of "cat."
while 'cat' in pets:
	pets.remove('cat')

print(pets)