from random import randint

class Die:
	"""A simple representation of a die."""
	def __init__(self, sides = 6):
		"""Initialize a die, with 6 as the default number of sides."""
		self._sides = sides

	def roll_die(self):
		"""Returns a number from one to the number of sides on the die."""
		return randint(1, self._sides)

d6 = Die()
for roll in range(10):
	print(d6.roll_die())

print('\n')
d10 = Die(10)
for roll in range(10):
	print(d10.roll_die())

print('\n')
d20 = Die(20)
for roll in range(10):
	print(d20.roll_die())