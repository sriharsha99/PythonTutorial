# def myfunc(*args):
#     return [x for x in args if x%2 == 0 ]

def myfunc(string):
    return [value.lower() if index%2 == 0 else value.upper() for (index, value) in enumerate(string)]

t = 'abc'
print (myfunc(t))
for i in t:
    print (i)