current_users = ['admin', 'bob', 'NoobMaster69', 'llamaguy', '55potato']
new_users = ['jeff80', 'Bob', 'Alex_70_The_Man', 'EpicDab27', 'Ur_Mom22']

lowercase_current_users = []
for current_user in current_users:
	lowercase_current_users.append(current_user.lower())

print(lowercase_current_users)

for new_user in new_users:
	if new_user.lower() in lowercase_current_users:
		print("This username is already taken. Please choose a new one.")
	else:
		print("This username is available.")