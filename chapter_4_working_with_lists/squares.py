squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)
print(squares)


# same thing as before, but more concise
squares = []
for value in range(1, 11):
	squares.append(value ** 2)
print(squares)

# hey check out these neat functions
print(min(squares))
print(max(squares))
print(sum(squares))

# resetting squares list
squares = []

# list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)