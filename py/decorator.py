

def new_decorator(func):

    def wrap_func():
        print ("some extra code before function")
        func()
        print ("some extra code before function")

    return wrap_func

def func_need_decorator():
    print ("i want to be decorated !!")


# dec = new_decorator(func_need_decorator)
# dec()

################
# Example: 2
################


import functools
def new_decorator1(func):
    @functools.wraps(func)
    def wrap_func(*args, **kwargs):
        print ("some extra code before function")
        func(*args, **kwargs)
        print ("some extra code before function")

    return wrap_func

def new_decorator2(func):
    @functools.wraps(func)
    def wrap_func(*args, **kwargs):
        print (f"argument length: {len(args[0])}")
        func(*args, **kwargs)
        print (f"argument length: {len(args[0])}")

    return wrap_func

@new_decorator2
@new_decorator1
def func_need_decorator1(name):
    print (f"{name} want to be decorated !!")

func_need_decorator1("sri")
