age = 17

if age < 2:
	status = 'baby'
elif age < 4:
	status = 'toddler'
elif age < 12:
	status = 'kid'
elif age < 20:
	status = 'teenager'
elif age < 65:
	status = 'adult'
elif age >= 65:
	status = 'elder'

if status == 'adult':
	print(f'You are an {status}.')
else:
	print(f'You are a {status}.')

# Although I could have used an else statement for the 65 or older part, using another elif is clearer when checking for a specific condition, like being 65 or older.