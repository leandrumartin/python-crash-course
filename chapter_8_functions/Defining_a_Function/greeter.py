# The part in the triple quotes is the docstring, which is what Python
#  looks for when it generates documentation for the functions in your programs.

def greet_user(username):
	"""Display a simple greeting."""
	print(f"Hello, {username.title()}!")

greet_user('jesse')
greet_user('sarah')