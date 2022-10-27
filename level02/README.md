# level02

This time, the home directory isn't empty : we find a `level02.pcap` file - a packet capture.

For comfort, retrieve it from our local machine using `scp` (secure copy) :

```
sudo scp -P 4242 level02@<SNOWCRASH_IP>:level02.pcap .
```

We can now analyze it using **Wireshark** (simply opening the file works)

We get a list of packet transmissions.
A `Right-click > Follow > TCP Stream` on the first packet allows us to view the full exchange.

The stream reveals the server prompts a user with `Password :`, to which the client responds with `ft_wandr...NDRel.L0L`

Further examination shows the value of the non-printable characters (showed here as `.`) is `7F`. `7F` is the hex value for the `DEL` key in ASCII.

We can now understand what the user typed :

```
ft_wandr[DEL][DEL][DEL]NDRel[DEL]L0L
```

The user must've made mistakes, and corrected them with the DEL key. We remove the letters typed before the DEL sequences - `ndr` and `l` :

```
ft_waNDReL0L
```

## The flag

We change users with `su flag02` using this password and run `getflag`. We get the level02 flag :

```
kooda2puivaav1idi4f57q8iq
```