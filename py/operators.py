word = 'abcdef'

# Enumerate
for item in enumerate(word):
    print (item)

a1 = [1,2,3,4]
a2 = [5,6,7,8]

# zip
for item in zip(a1, a2):
    print (item)

d = {'myKey': 345}
if 'myKey' in d:
    print (True)

if 345 in d.values():
    print (True)

from random import shuffle, randint

mylist = [3,4,5,6]
# shuffle the list, it's a inplace shuffle
shuffle(mylist)
print (mylist)

# random value with in the range
print (randint(0, 100))

# take the inputs from the user
result = input("enter the input") 
print (result)

