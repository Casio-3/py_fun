from pwn import *


s       = lambda data               :p.send(data)
sa      = lambda delim,data         :p.sendafter(delim, data)
sl      = lambda data               :p.sendline(data)
sla     = lambda delim,data         :p.sendlineafter(delim, data)
r       = lambda num=4096           :p.recv(num)
ru      = lambda delims,drop=True   :p.recvuntil(delims, drop)
itr     = lambda                    :p.interactive()
uu32    = lambda data               :u32(data.ljust(4, b'\0'))
uu64    = lambda data               :u64(data.ljust(8, b'\0'))
leak    = lambda name,addr          :log.success('{} = {:#x}'.format(name, addr))


def dbg(cmd=""):
    gdb.attach(p, cmd)
    pause()


context.log_level = 'DEBUG'
# context.terminal = ['tmux', 'splitw', '-h']

elf = context.binary = ELF('./pwn')
p = process(elf.path)

# ip, port = '127.0.0.1 8848'.split(' ')
# p = remote(ip, port)

itr()
