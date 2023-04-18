# 0x13. Firewall

## Concept
- ![image1](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/284/V1HjQ1Y.png)

> Your servers without a firewall…
- ![img](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/155/holbertonschool-firewall.gif)

> [What is a firewall](https://en.wikipedia.org/wiki/Firewall_%28computing%29)

## More Info
> As explained in the web stack debugging guide concept page, telnet is a very good tool to check if sockets are open with telnet IP PORT. For example, if you want to check if port 22 is open on web-02

```
sylvain@ubuntu$ telnet web-02.holberton.online 22
Trying 54.89.38.100...
Connected to web-02.holberton.online.
Escape character is '^]'.
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8

Protocol mismatch.
Connection closed by foreign host.
sylvain@ubuntu$
```
### Warning!
> Containers on demand cannot be used for this project (Docker container limitation)

> Be very careful with firewall rules! For instance, if you ever deny port 22/TCP and log out of your server, you will not be able to reconnect to your server via SSH, and we will not be able to recover it. When you install UFW, port 22 is blocked by default, so you should unblock it immediately before logging out of your server.

### Task
- Block all incoming traffic but
> Let’s install the ufw firewall and setup a few rules on web-01.

> Requirements:
>
> The requirements below must be applied to web-01 (feel free to do it on lb-01 and web-02, but it won’t be checked)
>
> Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
>
> 22 (SSH)
>
> 443 (HTTPS SSL)
> 
> 80 (HTTP)







