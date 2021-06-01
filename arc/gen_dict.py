import string
from itertools import product

dicts = string.digits + string.ascii_lowercase

def gen(n):
    for ran in product(dicts, repeat=4):
        yield ''.join(ran)

generator = gen(4)

print('Generating......')

with open('dict.dic','a+') as f:
    pre = 'minil'
    for i in generator:
        f.write(pre+i+'\n')

print('Task finished.')