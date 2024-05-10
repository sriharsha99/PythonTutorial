"""
for item in iterable:
    # Loop body
    if condition:
        # Do something
        break
else:
    # Execute this block if the loop completes without encountering a break statement
    # This block is optional
"""


# numbers = [1, 2, 3, 4, 5]
numbers = [0, 1, 2, 3, 4, 5]
for num in numbers:
    if num == 0:
        print("Zero encountered!")
        break
else:
    # this will run if we don't encounter break statement
    print("No zero found in the list.")

