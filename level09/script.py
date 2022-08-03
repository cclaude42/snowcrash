#!/usr/bin/env python3

hexdump = "66 34 6b 6d 6d 36 70 7c 3d 82 7f 70 82 6e 83 82 44 42 83 44 75 7b 7f 8c 89"

res = ""
for offset, hex in enumerate(hexdump.split()):
    n = int(hex, 16) - offset
    res += chr(n)

print(res)