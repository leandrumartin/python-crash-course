class Restaurant:
	"""Model for a restaurant."""
	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize attributes for a restaurant."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""Describe a restaurant."""
		print(self.restaurant_name)
		print(self.cuisine_type)

	def open_restaurant(self):
		"""Announce the restaurant's grand opening."""
		print(f"{self.restaurant_name.title()} is now open for business!")

panda_express = Restaurant('Panda Express', 'Chinese')
panda_express.describe_restaurant()

bonefish = Restaurant('Bonefish Grill', 'seafood')
bonefish.describe_restaurant()

olive_garden = Restaurant('Olive Garden', 'Italian')
olive_garden.describe_restaurant()