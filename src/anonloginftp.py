#!/usr/bin/python

import pexpect
import ftplib



def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'anonymous')
        print(" [*] " + hostname "FTP Anonymous Login Succeeded ")
        ftp.quit()
        return True
    expect Exception, e:
        print("[-] " + hostName + "Ftp Anonymous Logon Failed.")

host = raw_input("Enter the IP Address: ")
anonlogin(host)
