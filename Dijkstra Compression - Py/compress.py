# Margaret Walter
# CS2 Assn6
# File Compression program

import binascii as bn
import sys

class Node(letters, count):
    def __init__(self):
        self.data = count
        self.tag = letters
        self.left = None
        self.right = None

class Leaf(iden, count):
    def __init__(self):
        self.data = count
        self.tag = iden

class Tree():
    def __init__(self):
        self.key = {}
        self.head = None
        self.unattached = []

def huffpress(freq):
    tree = Tree()
    bench = len(freq)
    copy = freq{:}
    while len(freq) > 0: #Building the tree
        current = min(freq, key = freq.get) # Find the min value in freq
        new = Leaf(current, freq[current])
        del freq[current]                   # Deleting the current min to find the next one
        next = min(freq, key = freq.get)
        treeattach = |tree.head.data - new.data|
        branchattach = |min(tree.unattached) - new.data|
        newbranch = |freq[next] - new.data|
        options = [treeattach, branchattach, newbranch]
        if tree.head = None:
            tree.head = new
        elif min(options) == treeattach:
            right = tree.head
            tree.head = Node(right.tag + new.tag, right.data + new.data)
            tree.head.left = new
            tree.head.right = right
        elif min(options) == branchattach:
            # Min branch is closer to next min than main tree
            (d, p) = min(tree.unattached)
            newnode = Node(p.tag + new.tag, d + new.data)
            newnode.left = new
            newnode.right = p
            tree.unattached.remove((d,p))
            tree.unattached.append((newnode.data, newnode))
        else:
            nright = Leaf(next, freq[next])
            nbranch = Node(nright.tag + new.tag, nright.data + new.data)
            nbranch.left = new
            nbranch.right = nright
            tree.unattached.append((nbranch.data, nbranch)) #append a tuple of data & ptr to node
            del freq[next]
        current = min(freq, key = freq.get) #Redefining min 
        if min(tree.unattached) < current:
            #attach to main tree
            (dat, left) = min(tree.unattached)
            right = tree.head
            tree.head = Node(right.tag + new.tag, right.data + new.data)
            tree.head.left = left
            tree.head.right = right
            tree.unattached.remove((dat, left))
    #Building the key
    keyy = {}
    startstr = ''
    for i, j in copy.items(): #i is char, j is count
        startstr = ''
        while isinstance(tree.head, Leaf) == False:
            if i in tree.head.left:
                startstr += '0'
                tree.head = tree.head.left
            else: 
                startstr += '1'
                tree.head = tree.head.right
        keyy[i] = startstr

    return keyy

def encode(orig, keyy):
    startstr = ''
    for i in orig:
        startstr += keyy[i]
    output = bn.b2a_uu(startstr)
    return output
    

def savefile(ctext, keyy, filename):
    codedByte = sys.getsizeof(ctext)
    filename += 'HUFFMAN'
    with open(filename + 'KEY', 'w') as f:
        f.write(len(keyy))
        f.write(codedByte * 8)
        for i, j in keyy.items():
            f.write(i + ' ' + j)
    f.close
    with open(filename, 'w') as g:
        g.write(ctext)
    g.close()

def readfile(filename):
    with open(filename, 'r') as f:
        data = f.read().replace('\n', '').split('') # parsing characters into a list
    charcount = {n:data.count(n) for n in data} # counting characters & putting into dict
    f.close()
    return (data, charcount)

def statreport(orig, coded, keyy, filename):
    ''.join(orig)
    origByte = sys.getsizeof(orig)
    codedByte = sys.getsizeof(coded)
    charnum = len(keyy)
    print('Original file: ', filename)
    print('\tDistinct Characters: ', charnum)
    print('\tTotal Bytes: ', origByte)
    print('\tCompressed Text Length in Bytes: ', codedByte)
    print('Asymptotic Compression Ratio: ', (origByte/codedByte))


def compress(): #main
    filename = input("Enter a file to compress: ")
    (original, charfreq) = readfile(filename)
    keyy = huffpress(charfreq)
    encoded = encode(original, keyy)
    statreport(original, encoded, keyy, filename)
    savefile(encoded, keyy)

