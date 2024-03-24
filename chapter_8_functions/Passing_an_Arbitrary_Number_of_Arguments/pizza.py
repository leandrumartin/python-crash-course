# This function can accept an arbitrary number of arguments by making an empty tuple.

def make_pizza(*toppings):
	"""Print the list of toppings that have been requested."""
	print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Let's try it again, separating each item of the tuple.

print('\n')
def make_new_pizza(*toppings):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")

make_new_pizza('pepperoni')
make_new_pizza('mushrooms', 'green peppers', 'extra cheese')

# Parameters with an arbitrary number of arguments must be placed last.
print('\n')
def make_sized_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f"- {topping}")

make_sized_pizza(16, 'pepperoni')
make_sized_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')