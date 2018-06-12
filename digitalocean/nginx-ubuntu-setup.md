# Setting up Nginx on an Ubuntu Server

```
$ sudo apt-get update
$ sudo apt-get install nginx
```

```
$ sudo ufw app list
```

++ Mention output ++

If you haven't enabled SSL, allow in port 80. 
```
$ sudo ufw allow 'Nginx HTTP'
```

Verify by re-calling the status. 

```
$ sudo ufw status
```
Check your server status
```
$ systemctl status nginx
```
Source: https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04