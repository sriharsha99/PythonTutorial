

mylist = [num**2 for num in range(0, 11)]

print (mylist)


# if in list comprehension
mylist = [x  for x in range(0, 11) if x%2 == 0]
print (mylist)

# if else in list comprehension
mylist = [x if x%2 == 0 else 'ODD' for x in range(0, 11)]
print(mylist)

# nested loop in list comprehension
my_list = [x*y for x in [2,4,6] for y in [1,10,1000]]
print (my_list)


