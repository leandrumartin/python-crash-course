# You can make an argument optional by setting a blank default value and ignoring it if the user enters nothing.
def get_formatted_name(first_name, last_name, middle_name=''):
	"""Return a full name, neaty formatted."""
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)