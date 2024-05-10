# tuples are just like list except they are immutable


t = ('a', 'a', 'b')

# t.append('t')
# Error: AttributeError: 'tuple' object has no attribute 'append'

print (t.count('a')) # returns the count of 'a'
print (t.index('a')) # return index of the first element found


# t[0] = 'k' # immutable
# TypeError: 'tuple' object does not support item assignment