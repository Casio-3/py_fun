from pwn import *

"""
[+] Welcome!
[+] sha256(RJJw7sE9+?).binary.endswith('00000000000000000000')
[-] ?=
[+] wrong proof
"""

context.log_level = 'INFO'
alphabet = string.digits + string.ascii_letters


def main():
    p = remote('127.0.0.1', 10001)

    task = p.recvline_contains(b'sha256')
    print(task)
    # prefix = 'RJJw7sE9'
    prefix = re.search(r'\((\w+)\+', task.decode()).group(1)
    proof = brute(prefix)

    p.sendlineafter(b'[-] ?=', proof)
    p.interactive()


def trans_sha256_bin(data):
    from pwnlib.util.hashes import sha256sumhex
    return bin(int(sha256sumhex(str(data).encode()), 16))


def solver(prefix, x):
    return trans_sha256_bin(prefix + x).endswith('00000000000000000000')


def brute(_prefix):
    from pwnlib.util.iters import mbruteforce
    res = mbruteforce(lambda x: solver(_prefix, x), alphabet=alphabet, length=6, method='fixed')
    if res:
        return res.encode()


if __name__ == '__main__':
    main()
