# -*- coding: utf-8 -*-

import string
from collections import defaultdict

charset = string.printable.strip() + ' '

char_map = defaultdict(list)

for char1 in charset:
    for char2 in charset:
        key = chr(ord(char1) ^ ord(char2))
        if key in charset:
            char_map[key].append((char1, char2))


def is_banned(tup1, tup2):
    return True if list(set(tup1) & set(tup2)) else False


def x_print(tup):
    i = tup[0]
    j = tup[1]
    line = '{char1} ASCII: {ord1:>3d} <--xor--> {char2} ASCII: {ord2:>3d}'.format(char1=i, ord1=ord(i), char2=j,
                                                                                  ord2=ord(j))
    print(' |' + ' ' * 6, end='')
    print(line, end='')
    print(' ' * 6 + '|', end='\n')


def query(char, blacklist=''):
    # print(" ", "=" * 8, "'" + char + "'", "Can following composition", "=" * 8)
    print(f"  {8 * '='} '{char}' Can following composition {8 * '='}")
    results = char_map.get(char)
    buf = tuple(blacklist)
    for tup in results:
        if not is_banned(tup, buf):
            x_print(tup)
            buf += tup


if __name__ == '__main__':
    your_str = input('Your str: ')
    your_str = ''.join(set(your_str))
    banned = input('Blacklist: ')
    for c in your_str:
        query(c, banned)
