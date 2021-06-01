# -*- coding: utf-8 -*-
# @Author: Casio3
# @Description: Char XOR Map

import string
from collections import defaultdict

charset = string.printable.strip() + ' '

charmap = defaultdict(list)

for i in charset:
    for j in charset:
        key = chr(ord(i) ^ ord(j))
        if key in charset:
            charmap[key].append((i,j))

def query(char, blacklist):
    print(" ","="*8,"'"+char+"'","Can following composition","="*8)
    tups = charmap.get(char)
    buf = tuple(blacklist)
    for tup in tups:
        if not is_inter(tup, buf):
            x_print(tup)
            buf += tup


def x_print(tup):
    i = tup[0]
    j = tup[1]
    line = '{char1} ASCII: {ord1:>3d} <--xor--> {char2} ASCII: {ord2:>3d}'.format(char1=i,ord1=ord(i),char2=j,ord2=ord(j))
    print(' |'+' '*6, end='')
    print(line, end='')
    print(' '*6+'|',end='\n')


def is_inter(tup1, tup2):
    flag = list(set(tup1) & set(tup2))
    return True if flag else False

blacklist = ''

for char in charset:
    query(char, blacklist)
print(" ","="*8,"\t ~~o(*￣︶￣*)o~~\t","="*8)

"""
>>> string.whitespace
' \t\n\r\x0b\x0c'
>>> string.printable
'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
>>> string.printable.strip()
'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
"""