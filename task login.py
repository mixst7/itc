
login = input("введите логин: ")
password1 = input("введите пароль: ")
password2 = input("подтвердите пароль: ")
users = []

if not login.isdigit() and not login.isalpha():
	print('login prinyat')
	if password1 == password2:
		print('добро пожаловать')
		users.append((login, password1))
	else:
		print('пароли не совпадают')
else:
	print('login is invalid')

print(users)

