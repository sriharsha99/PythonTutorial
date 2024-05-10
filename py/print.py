print('His name is {}'.format('sri'))
print ('{} {} {}'.format('quick' , 'brown', 'fox'))
print ('{2} {1} {0}'.format('fox', 'brown', 'quick')) # we can re-arrange the arguments
print ('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

result = 100/77
print ("The result was {r}".format(r=result))

# floating format {value:width.precision f}

print ("The result was {r:1.5f}".format(r=result))
print ("The result was {r:10.5f}".format(r=result))




name ='sri'
print (f'hello , his name is {name}')