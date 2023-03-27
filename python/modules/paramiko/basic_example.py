import paramiko
from getpass import getpass
host = 'x.x.x.x'
username = input("  ")
password = getpass("  ")
session = paramiko.client.SSHClient()
session = set_missing_host.key.policy(paramiko.AutoAddPolicy())
session.connect(host,port=22,username=username)
stdin,stdout,stderr = session.exec_command('show version')
output = stdout.read().decode()
print(output)
ssh.close()
