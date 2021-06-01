with open('./cipher','r') as f:
    data = f.read()

Dict = {}
max = 1


for i in range(32,127):
    num = data.count(chr(i))
    if num:
        Dict[chr(i)] = num
        max = num if num > max else max

for key,value in Dict.items():
    print(key,':',value)

#Order = {}
#flag = ''
#for key,value in Dict.items():
#    if value != 1000 and value != 2000:
#        Order[key] = value

# 网上随便搜的一段排序
#a = sorted(Order.items(), key=lambda x: x[1], reverse=True)
#for j in a:
#    flag += j[0]

#print(flag)