a_zA_Z0_9_ASCII=list(range(48,58))+list(range(65,91))+list(range(96,123))
a_zA_Z0_9_Plus=list(range(32,58))+list(range(65,91))+list(range(90,127))
SYMBOL_ASCII=list(range(32,48))+list(range(58,65))+list(range(91,97))+list(range(123,127))

print ("[-] Waiting for create the dicts...")
dict_key=[]
dict_value = []

for i in SYMBOL_ASCII:
    for j in SYMBOL_ASCII:
        if i^j in a_zA_Z0_9_Plus:
            dict_key.append((i,j,chr(i),chr(j)))
            dict_value.append(chr(i^j))

dicts=dict(zip(dict_key,dict_value))
print ("[+] OK,The dicts is create")

#Here to change YourStr 
#example: 127.0.0.1|cat flag
YourStr = input("YourStr:")
print ("[-] YourStr is : %s\n"%(YourStr))
YourStr = ''.join(set(YourStr))
for i in YourStr:
    print ("============ ",i,"Can following composition ========")
    for k,v in dicts.items():
        if v == i and (k[0] in SYMBOL_ASCII) and (k[1] in SYMBOL_ASCII):
                print ('"%s" ^ "%s"'%(k[2],k[3]))