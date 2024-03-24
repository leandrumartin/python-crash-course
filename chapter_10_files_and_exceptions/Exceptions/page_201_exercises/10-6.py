try:
	num1 = int(input('\nGimme a number! '))
except ValueError:
	print("That ain't a numbah!")
else:
	try:
		num2 = int(input('\nGimme another number! '))
	except ValueError:
		print("That ain't a numbah!")
	else:
		print(f"\n{num1} + {num2} = {num1 + num2}")