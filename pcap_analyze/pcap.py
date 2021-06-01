# -*- coding: utf-8 -*-
# @Author: Casio3
import re

flag = []

#Ignore 'UnicodeDecodeError' when reading the pcapng file
with open("Sql.pcapng", "r", encoding = "utf-8", errors="ignore") as f:
    data = f.readlines()

for line in data:
    string = line.strip("\n")

#Grasp the target ASCII in Sqli sentences
    pattern1 = re.compile(r'(?<=,1\)\)\=)\d+')  #Zero-width positive lookbehind assertion
    target = re.findall(pattern1,string)
    if target:
        flag.append(''.join(target))

#To deal with the situation that all http status code is '200' in Blind Sqli, in which we should hold the right results
#For the giving example, we find 2 different response Content-Length:332 & 366
    pattern2 = re.compile(r"Content-Length: (\d+)")
    CL = re.findall(pattern2,string)
    if ''.join(CL) == str(332):
        flag.pop()

for i in flag:
    print(chr(int(i)),end="")