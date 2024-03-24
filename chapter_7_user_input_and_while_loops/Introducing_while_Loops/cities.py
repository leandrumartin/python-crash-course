# Let's use the 'break' statement to exit a loop without running any of the remaining code.
# Note that we don't actually have a condition for the 'while' loop.
# So, we can use this format to control which lines of code are executed.

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print(f"I'd love to go to {city.title()}!")

# Note: you can use the 'break' statment in any of Python's loops, such as 'for' loops.