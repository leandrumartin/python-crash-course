filename = 'learning_python.txt'

with open(filename) as file_object:
	print(file_object.read())

	print('\n')

	file_object.seek(0)
	for line in file_object:
		print(line.rstrip())

	print('\n')

	file_object.seek(0)
	lines = file_object.readlines()
for line in lines:
	print(line.rstrip())