

my_nums = [1,2,3,4,5]

def sqr(num):
    return num**2

def even(num):
    return num%2 == 0

# map()
print (list(map(sqr, my_nums)))
print (list(map(lambda x: x**2, my_nums)))

# filter()
print (list(filter(even, my_nums)))
print (list(filter(lambda x: x%2 == 0, my_nums)))

# reduce()
from functools import reduce
print (reduce(lambda x, y: x+y, my_nums, 100))

# square with lambda
square = lambda x: x**2
print (square(3))