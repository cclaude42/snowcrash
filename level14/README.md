# level14

There's nothing here - we wonder what to do. How about exploiting `getflag` itself ?

We want to do the same thing we did on `level13` : change the UID to trick `getflag` into thinking we're `flag14`.

We open `getflag` with Cutter. We see it's a rather complex mesh of conditions. We realize the following :

- There's a protection against reverse engineering done by calling `ptrace` we'll need to go around
- The conditional jump occurs at `<+74>`, we'll break there
- The rest of the program starts at `<+98>`, we'll jump there
- The check for `flag10` is right above the check for `flag14` ; by running as `flag10`, we can minimize how much we need to change
- The check for `UID == 3010` is at `<+546>` ; we'll break there and change the `eax` value.

We change users using the `level10` token :

```
su flag10
```

We run :

```
gdb getflag
```

We set our breakpoints and run the program :

```
disas main
break *main+74
break *main+546
run
```

We jump to `<+98>` to avoid the reverse-engineering safeguard ; the program runs until the next breakpoint, before the UID check.

We change the value of `eax` to 3014 (the flag14 UID) and finish executing the program :

```
jump *main+98
set $eax = 3014
next
```

## The flag

Getflag finishes executing and we get the `level14` flag :

```
7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
```