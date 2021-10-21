import hashlib
import itertools as its

# addStr = ''
knownMd5 = input('knownMd5:')
m = len(knownMd5)
n = int(input('textLen:'))

wordlist = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def md5(text):
    return hashlib.md5(str(text).encode('utf-8')).hexdigest()
def sha256(text):
    return hashlib.sha256(str(text).encode('utf-8')).hexdigest()

def generator(n,wordlist):
    dicts = its.product(wordlist, repeat=n)
    for gen in dicts:
        yield ''.join(gen)

for i in generator(n,wordlist):
    # i = i + addStr
    codeMd5 = md5(i)
    if codeMd5[:m] == knownMd5:
        print(i)

print("Task finished.")