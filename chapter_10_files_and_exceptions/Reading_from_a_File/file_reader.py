with open('pi_digits.txt') as file_object:
	contents = file_object.read()
# We include rstrip() here because there is a newline character at the end of every line.
# 	We remove it so that what we print will be truly identical to the file's contents.
print(contents.rstrip())

##########

filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

##########

# You can use readlines() to store the lines of a file for later processing, after you close the file.

filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())