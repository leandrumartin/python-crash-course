from restaurant import Restaurant

class IceCreamStand(Restaurant):
	"""An ice cream stand, based on the Restaurant class."""

	def __init__(self, restaurant_name):
		"""Initizialize an IceCreamStand instance."""
		super().__init__(restaurant_name, 'ice cream')
		self._flavors = ['chocolate', 'vanilla', 'strawberry']

	def display_flavors(self):
		print(f"Available flavors: {self._flavors}")

bobs_ice_cream = IceCreamStand("Bob's Ice Cream")
bobs_ice_cream.display_flavors()