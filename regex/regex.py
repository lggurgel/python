def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
         return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    
    return True


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('done')

print("-----------------------------------------------------------------")

import re

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_num_regex.search(message)
print(mo.group())

print("------------------------------------------------------------------")

phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_num_regex.search(message)
print(mo.group(1))
print(mo.group(2))
area, main = mo.groups()
print(area, main)

print("------------------------------------------------------------------")

phone_num_regex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
message = 'Call me at (415) 555-1011 tomorrow. (415) 555-9999 is my office.'
mo = phone_num_regex.search(message)
print(mo.groups())

"""
Characters with special mening: (to detect these chars as part of my pattern, I need to scape them with a backslash)

.  ^  $  *  +  ?  {  }  [  ]  \  |  (  )
"""

print("------------------------------------------------------------------")
""" The | operator """
hero_regex = re.compile(r'Batman|Tina Fey')
mo1 = hero_regex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = hero_regex.search('Tina Fey and Batman')
print(mo2.group())

print("------------------------------------------------------------------")

bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))


print("------------------------------------------------------------------")
""" The ? operator - match zero or one"""
bat_regex = re.compile(r'Bat(wo)?man')
mo1 = bat_regex.search('The Adventures of Batman')
print(mo1.group())
mo2 = bat_regex.search('The Adventures of Batwoman')
print(mo2.group())

print("------------------------------------------------------------------")
phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phone_regex.search('My number is 415-555-4242')
print(mo1.group())
mo2 = phone_regex.search('My number is 555-4242')
print(mo2.group())

print("------------------------------------------------------------------")
""" The * operator - match zero or more """
bat_regex = re.compile(r'Bat(wo)*man')
mo1 = bat_regex.search('The Adventures of Batman')
print(mo1.group())
mo2 = bat_regex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = bat_regex.search('The Adventures of Batwowowowoman')
print(mo3.group())

print("------------------------------------------------------------------")

""" The + operator - match one or more """
bat_regex = re.compile(r'Bat(wo)+man')
mo1 = bat_regex.search('The Adventures of Batman')
print(mo1 == None)
mo2 = bat_regex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = bat_regex.search('The Adventures of Batwowowowoman')
print(mo3.group())

print("------------------------------------------------------------------")

""" The {} operator - matching repetitions """
message = 'HaHaHaHaHaHa'
greedy_regex = re.compile(r'(Ha){3,5}')
mo1 = greedy_regex.search(message)
print(mo1.group())
nongreedy_regex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedy_regex.search(message)
print(mo2.group())

print("------------------------------------------------------------------")

""" The findall() function """
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
phone_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
print(phone_regex.findall(message))

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
phone_regex = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
print(phone_regex.findall(message))

print("------------------------------------------------------------------")

"""
Character Classes

\d - Any numeric digit from 0 to 9.

\D - Any character that is not a numeric digit from 0 to 9.

\w - Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)

\W - Any character that is not a letter, numeric digit, or the underscore character.

\s - Any space, tab, or newline character. (Think of this as matching “space” characters.)

\S - Any character that is not a space, tab, or newline.

"""

band_regex = re.compile(r'\d+\s\w+')
print(band_regex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

print("------------------------------------------------------------------")

""" The [] operator - for make own character classes """
""" The ^(caret) operator - make a negative character class """
vowel_regex = re.compile(r'[aeiouAEIOU]')
print(vowel_regex.findall('RoboCop eats baby food. BABY FOOD.'))
vowel_regex = re.compile(r'[aeiouAEIOU]{2,}')
print(vowel_regex.findall('RoboCop eats baby food. BABY FOOD.'))

# inside square brackets I do not need to scape . * ? ()
vowel_regex = re.compile(r'[^aeiouAEIOU.]')
print(vowel_regex.findall('RoboCop eats baby food. BABY FOOD.'))

print("------------------------------------------------------------------")

""" The caret ^ and dollar $ sign - match occur ant the beginning or at the end """
whole_number = re.compile(r'^\d+$')
print(whole_number.search('123456789'))

print(whole_number.search('12345d6789') == None)

print("------------------------------------------------------------------")

""" The . wildcard character - just for one character"""
at_regex = re.compile(r'.at')
print(at_regex.findall('The cat in the hat sat on the flat mat.'))

print("------------------------------------------------------------------")

""" Matching Everything with .* """
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = name_regex.search("First Name: Lucas Last Name: Gurgel")
print(mo.group(1), mo.group(2))