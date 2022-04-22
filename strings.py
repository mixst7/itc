'''
#1 problem

a = 'hello'.lower() +' ' + 'world'.upper()

print(a)

#2 problem

a = True
print (type(a))
a = str(a)
print (type(a))

#3 problem

print ('Github'.split(input('введите символ: ')))

#4 problem

a = 'Ботнет IPStorm , в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем'
print (a.replace('е', '3'))

#5 problem

a = input('enter your name: ')
b = input('enter your age: ')
c = input('enter you favorite movie: ')

print(f'hello {a}, {c} is cool movie')

#5 problem
a = 'Google создаст специальную команду для поиска багов в особо важных приложениях.'
print(len(a.split(' ')))


#6 problem

a = 'Самые важные собЫтия в миРе инфосека за сентябрь'
print('|'.join(a))


#7 problem

a = 'хакеры слили в сеть данные пакистанской энергетической компании k-Electric'
print(a.title())
'''


'''
a = input('say something: ')
mid = len(a)//2
print(a[:mid].upper(), a[mid:].lower())

'''

