def create_cubes(n):
    result = []

    for i in range(n):
        result.append(i**3)
    return result

for x in create_cubes(10):
    print (x)

# lets do it with generator

def create_cubes1(n):
    result = []

    for i in range(n):
        yield i**3

print (list(create_cubes1(10)))

for x in create_cubes1(10):
    print (x)

# let do fibonacii with generator

def fib(n):
    a = 1
    b = 1

    for i in range(n):
        yield a
        a, b = b, a+b

print (list(fib(5)))


# let destructure the generator

def simple_gen():
    for x in range(3):
        yield x

g = simple_gen()

print (next(g))
print (next(g))
print (next(g))
# print (next(g))

# generator expression instead of generator function

my_list = [1,2,3,4,5]

gencomp = (i for i in my_list if i > 3)

print ("printing from gencomp generator ... ")
for item in gencomp:
    print (item)

