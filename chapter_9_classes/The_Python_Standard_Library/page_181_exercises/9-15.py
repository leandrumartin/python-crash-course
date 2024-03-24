from random import choice

tickets = [1, 5, 2, 4, 7, 16, 32, 15, 23, 10, 'a', 'e', 't', 'c', 'k']

my_ticket = tickets[0]

tries = 0
winners = []
while my_ticket not in winners:
	winners = []
	while len(winners) < 4:
		to_add = choice(tickets)
		if to_add not in winners:
			winners.append(to_add)
	tries += 1
	print(winners)

print(f'Tries: {tries}')