"""Classes to represent users of a system."""

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

class Privileges():
	"""Privileges for an admin."""

	def __init__(self):
		self._privileges = ['can add post', 'can delete post', 'can ban user']

	def show_privileges(self):
		print(self._privileges)

class Admin(User):
	"""An admin, a special kind of user with special privileges."""

	def __init__(self, first_name, last_name, username, age, bio):
		"""Initialize an admin and their privileges."""
		super().__init__(first_name, last_name, username, age, bio)
		self.privileges = Privileges()

	def show_privileges(self):
		self.privileges.show_privileges()