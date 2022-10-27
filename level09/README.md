# level09

We're presented with an executable `level09` and a `token` file. The token can be read, but it has non-printable character. We run the executable :

```
./level09 aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

We get :

```
abcdefghijklmnopqrstuvwxyz{|}~�����������������
```

The executable seems to shift every letter of the input, increasingly by one character. This is called a **progressive cipher**, or a rolling cipher.

We run `hexdump -C token` and get :

```
00000000  66 34 6b 6d 6d 36 70 7c  3d 82 7f 70 82 6e 83 82  |f4kmm6p|=..p.n..|
00000010  44 42 83 44 75 7b 7f 8c  89 0a                    |DB.Du{....|
0000001a
```

We trim it a bit to keep the useful bytes :

```
66 34 6b 6d 6d 36 70 7c 3d 82 7f 70 82 6e 83 82 44 42 83 44 75 7b 7f 8c 89
```

Now, we just need a script to reverse the cipher. We write the following in Python :

```
#!/usr/bin/env python3

hexdump = "66 34 6b 6d 6d 36 70 7c 3d 82 7f 70 82 6e 83 82 44 42 83 44 75 7b 7f 8c 89"

res = ""
for offset, hex in enumerate(hexdump.split()):
    n = int(hex, 16) - offset
    res += chr(n)

print(res)
```

We run the script (on our local machine, the snow-crash VM doesn't have Python3) and we get :

```
f3iji1ju5yuevaus41q1afiuq
```

## The flag

We try it as password for `su flag09` and it works ! Now all that's left is running `getflag` :

```
s5cAJpM8ev6XHw998pRWG728z
```