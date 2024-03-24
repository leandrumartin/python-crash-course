tasty_foods = ['waffles', 'pancakes', 'french toast']
tasty_food = 'pancakes'

print(tasty_food == tasty_foods[1])
print(tasty_food != tasty_foods[1])
print(tasty_food == 'Pancakes')
print(tasty_food == 'Pancakes'.lower())

print('\n')

print('waffles' in tasty_foods)
print('waffles' not in tasty_foods)

print('\n')

number_0 = 8
number_1 = 12

print(number_0 < 10)
print(number_0 == 10)
print(number_0 > 10)
print(number_0 <= 10)
print(number_0 >= 10)

print('\n')

print(number_0 < 10 and number_1 > 10)
print(number_0 < 10 and number_1 < 10)
print(number_0 < 10 or number_1 < 10)