from user import User

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

me = Admin('leandru', 'martin', 'l.eandru', 18, 'hi')
me.privileges.show_privileges()