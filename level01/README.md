# level01

We take a look at the **password files** on the host machine.
A `cat /etc/passwd` reveals most passwords are encrypted (their hashes stored in the *shadow* files), but the `flag01` line stands out :

```
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
```

We store this line in a `passwd.txt` file on a machine with the **John the Ripper** cracking suite installed, and we simply run :

```
john passwd.txt
```

John reveals the cracked password for flag01 :

```
abcdefg
```

## The flag

We change users with `su flag01` and run `getflag`. We get the level01 flag :

```
f2av5il02puano7naaf6adaaf
```