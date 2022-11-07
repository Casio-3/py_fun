# with open('./cipher', 'r') as f:
#     data = f.read()
data = \
    """You do not have to pretend to be cold, I did not want to continue to pester you, the last time, really, 
    the last time, lend me 10 yuan sub, today is KFC Crazy Thursday finger sucking original chicken + gold crispy 
    chicken only 9.9 yuan, I really do not want to miss. """
Dict = {}
max_time = 1

for i in range(32, 127):
    num = data.count(chr(i))
    if num:
        Dict[chr(i)] = num
        max_time = num if num > max_time else max_time

for key, value in Dict.items():
    print(f"'{key}': {value}")

# Order = {}
# flag = ''
# for key,value in Dict.items():
#    if value != 1000 and value != 2000:
#        Order[key] = value

# a = sorted(Order.items(), key=lambda x: x[1], reverse=True)
# for j in a:
#    flag += j[0]

# print(flag)
