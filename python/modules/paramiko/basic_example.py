import paramiko
from getpass import getpass

host = 'x.x.x.x'
username = input("Enter username: ")
password = getpass("Enter password: ")

session = paramiko.client.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
session.connect(host, port=22, username=username, password=password)

stdin, stdout, stderr = session.exec_command('show version')
output = stdout.read().decode()
print(output)

session.close()
