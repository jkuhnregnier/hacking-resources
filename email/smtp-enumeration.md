## SMTP Enumeration

### Setting up a SMTP Server on DigitalOcean 
*For Ubuntu*

This will set up a new user account and copies the ssh-keys from the current user, root, to the new directory of the user.

```
$ ssh root@<ip address>
$ adduser <mailserver user>
$ usermod -aG sudo <mailserver user>
$ cp ~/.ssh/authorized_keys /home/<mailserver user>
$ exit
```

After that, you can disconnect as a root user and login with the `<mailserver user>` account.

```
$ ssh <mailserver user>@<ip address>

```

```
$ mkdir .ssh
$ sudo chown <mailserver user> authorized_keys
$ chmod 700 .ssh/
$ mv authorized_keys .ssh/
$ chmod 600 .ssh/authorized_keys
```

#### Install Postfix
```
$ sudo apt-get update
$ sudo apt-get install postfix

```

Change a few things in the postfix config. Settings will be added soon.

```
$ sudo nano /etc/postfix/main.cf
```

Create the virtual mapping of the e-mail accounts to the users. 

```
sudo nano /etc/postfix/virtual
```

### Enumerating SMTP Users
```
$ nc <ip address> 25
```

