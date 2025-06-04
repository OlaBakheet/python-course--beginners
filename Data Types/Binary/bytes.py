# immutable
# example 1 with numbers
b1 = bytes([70, 71, 72, 73])     # bytes if using numbers

print (b1)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# example 2 with a string
b2 = b'Welcome'                 # b if using string
print(b2)                       # output: b'Welcome'         # byte string not regular string

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# example 3
# to encode string to its corresponding numbers

text = "Ola"
byte_values = list(text.encode('utf-8'))
print(byte_values)         # output is [79, 108, 97]


text = "ola"
byte_values = list(text.encode('utf-8'))
print(byte_values)         # output is [111, 108, 97]

text = "OLA"
byte_values = list(text.encode('utf-8'))
print(byte_values)         # output is [79, 76, 65]
