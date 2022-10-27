# level13

There's a binary `./level13`. We execute it and get :

```
UID 2013 started us but we expect 4242
```

We open the binary with `gdb`

```
gdb level13
```

From the GDB prompt, we examine the program with :

```
disas main
```

We can see the program calls `getuid` at `<+9>`, compares it against `0x1092` (4242) at `<+14>`, and does a conditionnal jump at `<+19>`

From GDB, we can directly change the value of `%eax`, the register where `getuid` returns the user id. We run the following commands :

```
break *main+14
run
p $eax
```

This sets a breakpoint after the `getuid` return, runs the program, and shows the value of `%eax`. It's 2013, as expected. Now all we need to do is change it, and finish running the program :

```
set $eax = 4242
next
```

## The flag

The program finishes executing and prints our token :

```
2A31L79asukciNyi8uppkEuSx
```