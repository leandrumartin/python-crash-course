class User:
	def __init__(self, first_name, last_name, username, age, bio):
		"""Initialize attributes for a user profile."""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.username = username
		self.age = age
		self.bio = bio
		self.login_attempts = 0

	def describe_user(self):
		"""Describe a user profile."""
		print(f"\nName: {self.first_name} {self.last_name}")
		print(f"Username: {self.username}")
		print(f"Age: {self.age}")
		print(f"Bio: {self.bio}")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

me = User('leandru', 'martin', 'l.eandru', 18, 'yo whattup')
me.describe_user()

you = User('bob', 'joe', 'theJoeBob_99', 32, 'Hi!')
you.describe_user()

print(f'\n{me.login_attempts}')

me.increment_login_attempts()
print(me.login_attempts)
me.increment_login_attempts()
print(me.login_attempts)
me.increment_login_attempts()
print(me.login_attempts)
me.increment_login_attempts()
print(me.login_attempts)

me.reset_login_attempts()
print(me.login_attempts)