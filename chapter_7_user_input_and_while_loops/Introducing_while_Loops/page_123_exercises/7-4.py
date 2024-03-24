prompt = "\nWhat toppings would you like on your pizza?"
prompt += "\nEnter 'quit' to finish your order. "

desired_topping = ""
while desired_topping != 'quit':
	desired_topping = input(prompt)
	if desired_topping != 'quit':
		print("I'll add that to your pizza.")