# level00

A `README` file is missing from `/home`. You can see it if you watch the intranet's video on snow-crash.

A cat on the README file gives you a clue : "FIND the file that can be run by flag00"

We're looking for **a file owned, or readable by the user flag00**. We run :

```
find / -user flag00 2> /dev/null
```

We find two files : `/usr/sbin/john` and `/rofs/usr/sbin/john`. A cat on either of them gives us :

```
cdiiddwpgswtgt
```

This is a Caesar cypher. [dcode.fr](https://www.dcode.fr/caesar-cipher) detects it's a shift of 15, and allows us to get the flag00 password :

```
nottoohardhere
```

We change users with `su flag00` and run `getflag`. We get the level00 flag :

```
x24ti5gi3x0o12eh4esiuxias
```