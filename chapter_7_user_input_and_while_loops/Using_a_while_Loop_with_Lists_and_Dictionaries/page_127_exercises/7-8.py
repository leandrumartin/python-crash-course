sandwich_orders = ['reuben', 'sub', 'hot dog?', 'burger', 'tuna sandwich']
finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print(f'Making your {sandwich}...')
	finished_sandwiches.append(sandwich)

print('\n')
for finished_sandwich in finished_sandwiches:
	print(f'Here is your {finished_sandwich}!')