# Margaret Walter
# CS2 Assn6
# File Decompression program

import binascii as bn

startstr = ''
filename = input("File to decompress: ")
f = open(filename, 'rb')
readbytes = f.read()
bn.a2b_uu(readbytes)
f.close()
keyfile = input("Key: ")
translator = {}
with open(keyfile, 'r') as g:
        data = g.read().split('\n') # parsing characters into a list
g.close()
for i in data:
    i.split(' ') #-->2x2 array of characters & binary keys
    a = i[0] #char
    b = i[1]
    translator[b] = a

tempstr = ''
for j in readbytes: #parsing by bits
    if j in translator:
        startstr += translator[j]
        tempstr = ''
    elif tempstr in translator: #is the string of past n bits in the key?
        startstr += translator
        tempstr = ''
    else:
        tempstr += j #if not in the key, then add the next bit on to it ans try again

with open(filename + '.DECODED', 'w') as h:
        h.write(startstr)
h.close()