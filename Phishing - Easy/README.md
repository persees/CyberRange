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

## Target machine
Modify `C:\Windows\System32\drivers\etc\hosts` to contain an entry for "notmaliciousatall.com" pointing to localhost
```
127.0.0.1   notmaliciousatall.com
```

### Setup IIS server
```
Start > Control Panel > Programs and Features
(On the left) Turn Windows features on or off
Select Internet Information Services and Microsoft .NET
Click OK.
Copy the insertYourCredentials.html file to the IIS root directory `C:\inetpub\wwwroot\`
```
