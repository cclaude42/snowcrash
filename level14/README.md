# level14

```
su flag10
```

```
gdb getflag
```

```
disas main
break *main+74
break *main+546
run
jump *main+98
p $eax
set $eax = 3014
next
```

## The flag

Getflag finished executing and we get the `level14` flag :

```
7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
```