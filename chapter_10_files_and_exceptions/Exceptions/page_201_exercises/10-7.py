num1 = None
while not num1:
	try:
		num1 = int(input('\nGimme a number! '))
	except ValueError:
		print("That ain't a numbah!")
num2 = None
while not num2:
	try:
		num2 = int(input('\nGimme another number! '))
	except ValueError:
		print("That ain't a numbah!")
print(f"\n{num1} + {num2} = {num1 + num2}")