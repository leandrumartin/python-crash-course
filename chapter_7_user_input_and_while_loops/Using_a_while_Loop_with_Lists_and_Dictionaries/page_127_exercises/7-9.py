sandwich_orders = ['reuben', 'sub', 'hot dog?', 'pastrami', 'burger', 'pastrami', 'pastrami', 'pastrami', 'pastrami', 'tuna sandwich']
finished_sandwiches = []

pastramis = 0
for sandwich_number in range(len(sandwich_orders)):
	if sandwich_orders[sandwich_number] == 'pastrami':
		pastramis += 1

print('We are all out of pastrami. But uh-oh, Spaghetti-Os!', end=' ')
print(f'We have {pastramis} pastrami orders!')

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

print('\n')
while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print(f'Making your {sandwich}...')
	finished_sandwiches.append(sandwich)

print('\n')
for finished_sandwich in finished_sandwiches:
	print(f'Here is your {finished_sandwich}!')