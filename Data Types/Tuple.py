#immutable
#example 1
tuple1 = ( 'xyz', 77 , 3.1, 'noah', 80  )
tuple2 = (99, 'xyz')

print (tuple1)               # Prints the complete tuple
print (tuple1[0])            # Prints first element of the tuple
print (tuple1[1:3])          # Prints elements of the tuple starting from 2nd till 3rd
print (tuple1[2:])           # Prints elements of the tuple starting from 3rd element
print (tuple2 * 2)       # Prints the contents of the tuple twice
print (tuple1 + tuple2)   # Prints concatenated tuples
