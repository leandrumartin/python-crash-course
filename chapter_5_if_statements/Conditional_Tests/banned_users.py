banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish.")
elif user in banned_users:
	print(f"{user.title()}, you are not allowed to post here!")