filename = 'alice.txt'

with open(filename, encoding='utf-8') as f:
	print(f.read().count('the '))