filenames = ('cats.txt', 'guineapigs.txt', 'dogs.txt')

for filename in filenames:
	try:
		with open(filename) as f:
			print(f.read())
	except FileNotFoundError:
		pass