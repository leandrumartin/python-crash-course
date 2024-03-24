def print_models(unprinted_designs, completed_models):
	"""Simulate printing each design until none are left.
	   Move each design to completed_models after printing.
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""Show all the models that were printed."""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodechedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Now, the list unprinted_designs is empty.
print(f'\n{unprinted_designs}')

# If you want to keep the original list of unprinted designs intact, you can use a copy of the list as the argument.

print('\n')
unprinted_designs = ['phone case', 'robot pendant', 'dodechedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

print(f'\n{unprinted_designs}')