# Local
# Enclosing
# Global
# Built-in


name = "This is global"

def greet():

    # what if you want to modify the global variable
    global name

    # Enclosing
    name = 'sammy'

    def hello():
        # Local
        name = 'IM A LOCAL'
        print ('Hello ' + name)
    hello()

greet()