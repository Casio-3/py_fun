# -*- coding: utf-8 -*-
import re

flag = []

with open("access.log", "r", encoding="utf-8", errors="ignore") as f:
    data = f.readlines()

for line in data:
    string = line.strip("\n")

    pattern1 = re.compile(r'\d+(?=,sleep\(2\),1\)--\+ HTTP/1\.1\" 200 377)')
    target = re.findall(pattern1, string)
    if target:
        flag.append(''.join(target))

for i in flag:
    print(chr(int(i)), end="")

"""awk.sh alternatively
awk -F '[=,]' '/flag.*?377/ {printf "%c", $5}' access.log | base64 -d
"""