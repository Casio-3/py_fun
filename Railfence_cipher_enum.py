def decode(cipher):
    length = len(cipher)
    field = []
    for key in range(2,length):
        if(length % key == 0):
            field.append(key)
    for f in field:
        b = length // f
        result = {x:'' for x in range(b)}  
        for i in range(length):  
          a = i % b;  
          result.update({a:result[a] + cipher[i]})  
        d = ''
        for i in range(b):  
          d = d + result[i]  
        print('分为'+str(f)+'栏时，解密结果为：'+d)
        
if __name__ == '__main__':
    cipher = input("Input the cipher to be decoded:")
    decode(cipher)