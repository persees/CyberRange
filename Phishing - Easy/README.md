
# Configuration

## Postfix
```
sudo apt install postfix
sudo cp /etc/postfix/main.cf /etc/postfix/main.cf.backup
sudo vim /etc/postfix/main.cf
# Edit inet_interfaces to be equals to loopback-only
sudo systemctl enable postfix
sudo systemctl start postfix
```


