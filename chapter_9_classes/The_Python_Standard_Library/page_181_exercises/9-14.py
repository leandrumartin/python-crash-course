from random import randint

tickets = [1, 5, 2, 4, 7, 16, 32, 15, 23, 10, 'a', 'e', 't', 'c', 'k']

print('If your ticket is any of the following, pick up your raffle prize:')
for winner in range(4):
	print(tickets.pop(randint(1, len(vals) - 1)))