# import function.py
from function import *
import getpass
import bcrypt
import os
import subprocess
import sys

# load art
with open("art/art.txt", "r") as art_file:
    art = art_file.read()  # Read the entire contents of the file

    

# password  SalukiSuccess

subprocess.run(["clear"])
print(art)
HashedPassword = b"$2a$12$2z.vvLziOtUHUgSaP8IIBeJBbGZvkxxF0K4bLU6.wvR3O75fYzM.u"
input_password = getpass.getpass("Enter the password: ").encode()
if bcrypt.checkpw(input_password, HashedPassword):
    print("Access granted.")
    # Script logic here
else:
    print("Access denied.")
    exit()






choice = "Add(1) Delete(2) Browse(3) Exit(4)"
#main
while(True):   
    subprocess.run(["clear"])

    
    print(art)
    print(choice)
    response = str(input())
    if response =='1':
        add()
    elif response =="2":
        Delete()
    elif response == "3":
        browse()
    elif response == "4":  
        sys.exit(0)