"""A class to represent a user of a system."""

class User:
	def __init__(self, first_name, last_name, username, age, bio):
		"""Initialize attributes for a user profile."""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.username = username
		self.age = age
		self.bio = bio

	def describe_user(self):
		"""Describe a user profile."""
		print(f"\nName: {self.first_name} {self.last_name}")
		print(f"Username: {self.username}")
		print(f"Age: {self.age}")
		print(f"Bio: {self.bio}")