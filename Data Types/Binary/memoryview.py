# example 1
data = bytearray(b'Hello, world!')
view = memoryview(data)
print(view)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#example 2
data = b'Hello, world!'
# Creating a view of the last part of the data
view = memoryview(data[7:])
print(view)
