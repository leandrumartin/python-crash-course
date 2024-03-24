# This function accepts an arbitrary number of keyword arguments by making an empty dictionary
#  and storing the keyword arguments as key-value pairs.

def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('leandru', 'martin',
							location='Makanda',
							school='Saint Louis University',
							DMECRA_designation_number = 14)

print(user_profile)