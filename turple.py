'''
#problem 0
a = [('name'), ('age'), ('last name'), ('city'), ('food')]
print(a)

#problem 1
a = (123, True, 'hello')
print(a.index(123))
print(a.index(True))
print(a.index('hello'))

print(a[::])

#problem 2
a = (True, 1, 'str', ['list'], ('turple'))
print(a)

#problem 3
a = ['Asyl', 'Semetei', 'Adam', 'Azat', 'Tima']
b = ' '.join(a)
print(b)

#problem 4
a = ['the', 'a', 5, 4.3]
b = ['last', 'air', 'bender']

a.extend(b)
print(a)

#problem 5
names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  
'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',
'Jackson', 'Oskar', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]

print(names.count('Jack'))


#problem 6
names = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  
'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 
'Jackson', 'Oskar', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]

print(names)
names.remove('Oskar')
print(names)


#problem 7
a = []
b = ('Merei', '1997', 'Python')
a.extend(b)
print(a)


#problem 8
pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", 
"tuple", "list", "None", True, False]

print(pythonList.index("loop"))
print(pythonList)
pythonList.pop(6)
print(pythonList)

#problem 9
a = [123, 321, 2, 543, 64, 463, 234, 867, 6234, 63246, 3, 43]

print(len(a))
print(a[0] * a[1] * a[2] * a[3] * a[4] * a[5] * a[6] * a[7] * a[8] * a[9] * a[10] * a[11])

#problem 11
pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", 
"tuple", "list", "None", True, False]
print(pythonList[1:3])
'''
