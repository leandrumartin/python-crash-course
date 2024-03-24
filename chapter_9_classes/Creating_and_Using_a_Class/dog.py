# By convention, a capitalized name refers to a class.
class Dog:
	"""A simple attempt to model a dog."""

	# Python runs the __init__ method automaticaly when we create a new instance based on this class.
	# The self parameter is required in the method definition and must come before other parameters.
	def __init__(self, name, age):
		"""Initialize name and age attributes."""
		# Any variable prefixed with self is available to every method in the class.
		self.name = name
		self.age = age

	def sit(self):
		"""Simulate a dog sitting in response to a command."""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Simulate rolling over in response to a command."""
		print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

print('\n')
your_dog = Dog('Lucy', 3)

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")

your_dog.sit()
your_dog.roll_over()