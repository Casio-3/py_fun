import string
"""
digits:'0123456789'
punctuation:'!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'
ascii_letters:'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
whitespace:'\t\n\r\x0b\x0c'
printable:'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
制表、换行、返回、换页、垂直制表
"""

print(string.hexdigits)

# print(string.digits)
# print(string.punctuation)
# print(string.ascii_letters)
# print(string.whitespace)
print(string.printable)
