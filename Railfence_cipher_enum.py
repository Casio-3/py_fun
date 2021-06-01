#-*- coding=utf-8 -*-
# def encode():
#     plain = input('输入明文：')
#     n = int(input('输入每组字数:'))
#     ans = ''
#     for i in range(n):
#         for j in range(int(plain.__len__()/n + 0.5)):
#             try:
#                 ans += plain[j*n+i]
#             except:
#                 pass
#     return ans

# def decode():
#     plain = input('输入密文：')
#     result = []
#     for n in range(2,plain.__len__()-1):
#         ans = ''
#         for i in range(n):
#             for j in range(int(plain.__len__() / n + 0.5)):
#                 try:
#                     ans += plain[j * n + i]
#                 except:
#                     pass
#         if len(ans) == len(plain):  #只打印有效key
#             print(ans)
#         if ans[-1] == '}':
#             result.append(ans)
#     if result:
#         print("Maybe you want...:",result)


# if __name__ == '__main__':
#     print('栅栏密码加密/解密')
#     choice = input('功能选择：\n1：加密\n2：解密\n')
#     # 加密
#     if choice == '1':
#         print(encode())
#     # 解密
#     elif choice == '2':
#         decode()
#     else:
#         print('choice error!')


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