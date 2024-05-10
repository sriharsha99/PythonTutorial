# print (3/2)
# print (7/4)

print ((0.1 + 0.2) - 0.3) # this not equal to zero

string = "hello"
print (string[-1])
print (string[-5])

print (string[::])


# We could also insert new elements into the list using slicing as follows:
numbers =  [1, 10, 20, 30, 5, 6, 7, 8, 9]
numbers[4:4] = [40, 50]
print (numbers)

# slicing using indexing sequence 
str1 ="Geeks for Geeks !"
print(str1[-1 : -12 : -2])

# reverse of the string
for i in str1[::-1]:
    print (i)

# step with negative start & stop without step
k = [1,2,3,4,5,6]
print ("*"*5)
print (k[-1: -5])
print ("*"*5)

# here we are getting empty, because we are defining negative step size
# By default it will take positive step size

print (k[-1:-5:-1])


# Stride or step

a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']

# start:stop:step
# start index is included
# stop index is not included
# step if step is positive
#            1. it is forward direction
            # 2. start is included
            # 3. end is not included
#       else step is negative
#            it is backward direction
             # 2. start is included
            # 3. end is  not included

# Note: Both are same, sorry for the confusion

# print (a[0:6:2])


print (a[5:3:-1])