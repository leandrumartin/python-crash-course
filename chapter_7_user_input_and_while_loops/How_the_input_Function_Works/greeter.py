name = input("Please enter your name: ")
print(f"\nHello, {name}!")

# How to write multi-line prompts
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")