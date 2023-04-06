# Requirements
- Target machine connected to Microsoft Defender Endpoint

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

## SendMail.py script
Sending an email from the attacker machine to the target machine
`sendMail.py -s <sender@mail> -r <receiver@mail>`
