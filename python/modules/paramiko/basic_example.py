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

# Explanation:

# This is a Python script that uses the paramiko library to connect to an SSH server and execute a command remotely. 
# Here's what the code does, line by line:

# 1. Imports the paramiko library, which provides an implementation of the SSH protocol in Python, and the getpass function from the getpass module, which allows you to securely prompt the user for a password without echoing it to the console.

# 2. Sets the value of the host variable to the IP address or hostname of the SSH server you want to connect to.

# 3. Prompts the user to enter their username and password. The input() function is used to get the username, and the getpass() function is used to get the password, without displaying it on the console.

# 4. Creates an instance of the SSHClient class from the paramiko.client module.

#         Sidenote:

#         You cannot replace session = paramiko.client.SSHClient() with session = SSHClient() directly, because SSHClient() is not defined in the current namespace.
#         In the script, the SSHClient() class is defined in the paramiko.client module, which is why you need to qualify it with paramiko.client. when you create an instance of it.  

#         If you want to avoid typing the paramiko.client prefix every time you use SSHClient(), you can import the class directly into your script by adding the following line at the top:

#         from paramiko.client import SSHClient

#         Then you can create an instance of the class like this:

#         session = SSHClient()


# 5. Sets the policy for automatically adding new SSH host keys to the AutoAddPolicy(). This is a security measure to prevent man-in-the-middle attacks, and the AutoAddPolicy() policy will automatically add new host keys to the client's list of known hosts without prompting the user.

# 6. Connects to the SSH server specified by the host variable, using the provided username and password. The port parameter specifies the port number to use for the SSH connection, which defaults to 22.

# 7. Executes the command "show version" on the SSH server using the exec_command() method of the SSHClient object. This method returns three file-like objects: stdin, stdout, and stderr. In this case, we only care about the output of the command, which is captured in the stdout object.

#         Sidenote:  In Python, a file-like object is any object that behaves like a file, in the sense that it supports reading from or writing to it using methods like read(), write(), readline(), writelines(), etc.

#         In the statement stdin, stdout, stderr = session.exec_command('show version'), the = operator is used to assign the result of the exec_command() method call to three variables stdin, stdout, and stderr simultaneously.

#         This is called multiple assignment or unpacking, and it is a convenient way to assign multiple values to multiple variables in a single line of code.

#         The exec_command() method returns a tuple of three file-like objects, in the order stdin, stdout, and stderr. The three variables on the left-hand side of the = operator are also a tuple of three variable names, in the same order.

#         By using multiple assignment, the values of the three file-like objects are automatically unpacked and assigned to their corresponding variable names.

#         So after the statement stdin, stdout, stderr = session.exec_command('show version') is executed, the stdin variable will reference the file-like object representing the standard input stream of the executed command, stdout will reference the file-like object representing the standard output stream, and stderr will reference the file-like object representing the standard error stream.


# 8. Reads the output of the command from the stdout file-like object and decodes it from bytes to a string using the decode() method.

#         stdout is a file-like object that represents the standard output stream of the command executed using exec_command() method of paramiko's SSHClient() class.

#         To read the output of the command, you need to call the read() method of stdout, which reads all the data from the stream and returns it as a byte string.

#         The decode() method is then called on the byte string returned by read(), which converts it from a byte string to a Unicode string using the default encoding of the system.

#         The decode() method is necessary because the read() method returns a byte string, which represents the data in a binary format. To convert the byte string to a human-readable string, you need to decode it into Unicode. The choice of encoding depends on the encoding used by the command's output. In this case, the default encoding of the system is used.

#         So the overall effect of the expression stdout.read().decode() is to read the output of the command executed using exec_command(), convert it from a byte string to a Unicode string, and return it as the value of the output variable. The output variable can then be printed to the console using the print() function.

# 9. Prints the output of the command to the console using the print() function.






