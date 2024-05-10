

l = [1,2,2,3,4,5,6,7]

# l.pop(<index>)
k = l.pop(0)
print (k)
print (l)


l.remove(2)
print (l)
# l.remove(<value>) # remove first occurence of the element

# inplace list sorting
new_list = ['a', 'e', 'x', 'b', 'c']
new_list.sort()
print (new_list)

p = new_list.sort() # doesnt return anything, all the sorting is done inplace
print (p) 



print (new_list.reverse()) # inplace reverse
print (new_list)