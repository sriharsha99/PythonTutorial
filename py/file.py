myfile = open('./abc.txt')
print (myfile.read())

# for this print it doesn't print anything because the cursor
# is at the end of the file
print (myfile.read())

# inorder to move the read cursor back to the tip of
# the file, we do seek(0)

myfile.seek(0)

contents = myfile.read()
print (contents)


myfile.seek(0)

print (myfile.readlines())
myfile.close() # we need to close this file other wise it will be in 
               # in open state. if some one tries to delete it, they
               # will get error like file is already open.

with open('abc.txt', mode='r') as my_new_file:
    contents = my_new_file.read() # here i don't bother about closing the file, with will take care of it.

# r+ (Read and Write):
# Opens the file for both reading and writing.
# The file pointer (or cursor) is positioned at the beginning of the file.
# If the file doesn't exist, it raises a FileNotFoundError.
# If the file exists, the data will be overwritten if you write to it.
# You can read from and write to the file using methods like read(), write(), seek(), etc.


# w+ (Write and Read):
# Opens the file for both reading and writing.
# If the file exists, it truncates the file to zero length, meaning it deletes all existing content.
# The file pointer is positioned at the beginning of the file.
# If the file doesn't exist, it creates a new file.
# You can read from and write to the file using methods like read(), write(), seek(), etc.


with open('abc.txt', mode='w+') as my_new_file:
    contents = my_new_file.read() # here i don't bother about closing the file, with will take care of it.

# 'w' (Write Mode):
# Opens the file for writing only.
# If the file exists, it truncates the file to zero length, meaning it deletes all existing content.
# If the file doesn't exist, it creates a new file.
# The file pointer is positioned at the beginning of the file.
# You cannot read from the file using 'w' mode.



# 'w+' (Write and Read Mode):
# Opens the file for reading and writing.
# If the file exists, it truncates the file to zero length, meaning it deletes all existing content.
# If the file doesn't exist, it creates a new file.
# The file pointer is positioned at the beginning of the file.
# You can both read from and write to the file using 'w+' mode.


# mode='r' read only
# mode='w' is write only (will overwrite files or create new)
# mode='a' is append only (will add on to files)
# mode='r+' is reading and writing
# mode='w+' is writing and reading (Overwrites existing files or creates a new file)


# cleaning the content
with open('abc.txt', mode='w') as f:
    f.write("fist line")

# Lets do read & write of the file

def simple_func():

    with open('abc.txt', mode='r') as f:
        print (f.read())

    print ("reading ...")

    with open('abc.txt', mode='a') as f:
        print (f.write('second line'))

    print ("writing ...")

    with open('abc.txt', mode='r') as f:
        print (f.read())

    print ("reading ...")

simple_func()