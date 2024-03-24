filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	# We use strip() to remove the spaces at the left side of the lines, and the newline characters on the right.
	pi_string += line.strip()

print(f'{pi_string[:52]}...')
print(len(pi_string))