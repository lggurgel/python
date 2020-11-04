condition = True

x = 1 if condition else 0

print (x)

#########################################################################

num1 = 10_000_000_000
num2 = 100_000_000

total = num1 + num2

print(f'{total:,}')

#########################################################################
# Context managers
try:
    with open('text', 'r') as f:
        file_contents = f.read()

    words = file_contents.split(' ')
    word_count = len(words)
    print(word_count)

except:
    print("Error")

#########################################################################

names = ['Mat', 'John', 'Jesuis', 'Horus']

for index, name in enumerate(names, start=1):
    print(index, name)

names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

for name, hero, universe in zip(names, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')

#########################################################################
# Unpacking

a, _ = (1, 2)
print(a)

a, b, *_, d = (1, 2, 3, 4, 5, 6, 7, 8)
print(a)
print(b)
# print(c)
print(d)

#########################################################################

class Person():
    pass

person = Person()

first_key = 'first'
first_val = 'Corey'

setattr(person, first_key, first_val)
first = getattr(person, first_key)
print(first)

person = Person()

person_info = {'first': 'Lucas', 'last': 'Gurgel'}

for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))


#########################################################################

from getpass import getpass

username = input('Username: ')
password = getpass('Password: ')

print('Logging in...')

# python -m password (running modules)