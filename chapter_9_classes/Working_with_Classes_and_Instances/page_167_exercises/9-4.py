class Restaurant:
	"""Model for a restaurant."""
	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize attributes for a restaurant."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Describe a restaurant."""
		print(self.restaurant_name)
		print(self.cuisine_type)

	def open_restaurant(self):
		"""Announce the restaurant's grand opening."""
		print(f"{self.restaurant_name.title()} is now open for business!")

	def set_number_served(self, number):
		self.number_served = number

	def increment_number_served(self, increment):
		self.number_served += increment

panda_express = Restaurant('Panda Express', 'Chinese')
panda_express.describe_restaurant()
panda_express.open_restaurant()

print(panda_express.number_served)

panda_express.number_served += 1
print(panda_express.number_served)

panda_express.set_number_served(3)
print(panda_express.number_served)

panda_express.increment_number_served(3)
print(panda_express.number_served)