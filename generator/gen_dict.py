import string
from itertools import product

wordlist = string.digits + string.ascii_lowercase


def generator(n):
    for element in product(wordlist, repeat=n):
        yield ''.join(element)


print('Generating......')

with open('dict.dic', 'a+') as f:
    prefix = 'minil'
    for i in generator(4):
        f.write(prefix + i + '\n')

print('Task finished.')
