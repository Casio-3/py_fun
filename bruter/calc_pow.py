import hashlib
import sys
import string
from pwnlib.util.iters import mbruteforce

# run under linux

charset = string.printable
charset = string.ascii_letters + string.digits


def pre_md5(text, prelen=0):
    return hashlib.md5(str(text).encode('utf-8')).hexdigest()[:prelen]


def pre_sha256(text, prelen=0):
    return hashlib.sha256(str(text).encode('utf-8')).hexdigest()[:prelen]


def suf_md5(text, suflen=0):
    return hashlib.md5(str(text).encode('utf-8')).hexdigest()[-int(suflen):]


def suf_sha256(text, suflen=0):
    return hashlib.sha256(str(text).encode('utf-8')).hexdigest()[-int(suflen):]


task = 'cd0d65'
s = ''

if len(sys.argv) > 1:
    task = sys.argv[1]

# sha256(xxxx+s)[:6] == hash
Proof = mbruteforce(lambda x: suf_sha256((x + s), len(task)) == task, alphabet=charset, length=4, method='fixed')

if Proof:
    print(suf_sha256(Proof))
    print(f"sha256({Proof + s})[:6] == {task}")
else:
    print("Not found.")
