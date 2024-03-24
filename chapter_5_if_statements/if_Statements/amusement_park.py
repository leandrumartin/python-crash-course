age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
else:
	price = 20

# below is the same thing, but demonstrating that an "else" function isn't necessary, and sometimes another elif is clearer if there's a specific final condition you're testing for.

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
elif age >= 65:
	price = 20

print(f"Your admission cost is ${price}.")