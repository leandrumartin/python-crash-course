dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Trying to change any of the values will result in an error. Since this list uses parenthesis (and not square brackets) it is a tuple, which is immutable!

print('\n')
for dimension in dimensions:
	print(dimension)

# Though you can't modify a tuple, you can assign a new value to a variable representing a tuple.

print('\n')
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)