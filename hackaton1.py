'''
products = ['яблоко', 'груша', 'арбуз', 'банан', 'мандарин']
print(products)
b = len(products) - 1
a = int(input('add your index: '))
if a > b:
	print('invalid index')
else:
	products.pop(a)
	print(products)
'''

'''
points = 0
print('Your current points')
print('choose right version:  \n1)3+8. 2)7+3. 3)6+7.')
quest1 = int(input('Where is 10: '))
if quest1 == 2:
	points += 1
	print('Right')
else:
	print('Not right')

print('choose right version:  \n1)12+42. 2)34+6. 3)2+7.')
quest2 = int(input('where is 9: '))
if quest2 == 3:
	points += 1
	print('Right')
else:
	print('Not right')

print('choose right version:  \n1)15+3. 2)24+5. 3)3+11.')
quest3 = int(input('where is 29: '))
if quest3 == 2:
	points += 1
	print('Right')
else:
	print('Not right')

print('Your total points', points)

if points == 3:
	print('pass')
elif points == 1 or points == 2:
	print('you have failed, try again')
else:
	print('you have answered 0 right')
'''


'''
a = ['', 3, 4, True, ('Juk'), ['dusk'], 'day', 5, 6, False]
b = int(input('Choose number from 1 to 9: '))
print(a[b:])
'''
