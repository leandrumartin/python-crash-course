def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# Order matters!
describe_pet('harry', 'hamster')

# You can use keyword arguments to avoid this mistake.
print("\nUsing keyword arguments:")
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# You can define a default value for each parameter.
def describe_pet_new(pet_name, animal_type='dog'):
	"""Display information about a pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

print("\nUsing a new function with a default animal type:")
describe_pet_new('willie')
describe_pet_new(pet_name='harry', animal_type='hamster')

# This next function call will cause an error, because it doesn't enter the necessary number of arguments.
describe_pet()