import binascii
crc = 0xb11477fe
dic = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
for a in dic:
    for b in dic:
        for c in dic:
            for d in dic:
                string = a+b+c+d
                str_crc = binascii.crc32(string.encode())
                if(str_crc == crc):
                    print(string)