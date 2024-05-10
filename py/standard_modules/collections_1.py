from collections import Counter
# one
mylist = [1,1,1,2,2,2,3,3,3,3]
mylist1= ['a', 'a', 10,10,10]
print (Counter(mylist))
print (Counter(mylist1))

# two
print (Counter('aalskdjfdddefefff'))

# three
sentence = "How many times each word show up in this sentence with a word"

print (Counter(sentence.lower().split()))

# four
letters = "aaaaabbbbbbcccccccddddddddddd"
c = Counter(letters)
print (c)

print (c.most_common())

# most common use cases

# sum(c.values)   # total of all counts
# c.clear()       # reset all counts
# list(c)         # list unique elements
# set(c)          # convert to set
# dict(c)         # convert to regular dictionary
# c.items()       # convert to a list of (elem, cnt) pair
# # Counter(dict())
# c.most_common[:-n-1:-1] # n least common elements
# c += Counter()     # remove zero and negative counts



from collections import defaultdict

# let take normal dict

k = {}
# k['a'] will be giving some 

# so inorder to deal with some default value for the unknown key
# we use defaultdic

d = defaultdict(lambda : 0)

d['correct'] = 100

# here it will print default value 0
print (d['wrong_key'])



