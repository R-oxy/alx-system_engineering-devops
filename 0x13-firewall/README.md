# 0x13. Firewall

## Background Context

If you've ever wondered what your servers are like without a firewall, this project is for you. It's crucial to understand how firewalls work to protect your systems and data.

## Resources

- [What is a firewall](#)
  
## More Info

I've found that `telnet` is an excellent tool for debugging and checking if sockets are open. For instance, if I want to check if port 22 is open on `web-02`, I run:

```bash
telnet web-02.teflontech.dev 22
```

The output shows that the connection is successful, indicating that the port is open. Now, if I try connecting to port 2222:

```bash
telnet web-02.teflontech.dev 2222
```

The connection never succeeds, and I have to kill the process with `ctrl+c`.

This `telnet` approach is not just for this project; it's a general debugging technique for any situation where two software components need to communicate over sockets.