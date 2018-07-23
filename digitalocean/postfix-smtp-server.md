# Setting up Postfix as an SMTP Server on Ubuntu 14.04

```
sudo apt-get install mailutils
```

```
sudo nano /etc/postfix/main.cf
```

In the config, scroll down and go 

```
mailbox_size_limit = 0
recipient_delimiter = +
inet_interfaces = all
```

And set `inet_interfaces` to localhost. And restart the postfix server. 

```
sudo service postfix restart
```



Source: https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-postfix-as-a-send-only-smtp-server-on-ubuntu-14-04