#!user/bin/python

import socket
import os
import sys

def checkVulns();
    f = open(filename, "r");
    for line in f.readLines():
        if line.strip("\n") in banner:
            print "server is vulnerable: " + banner.strip("\n")

def retBanner():
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip.port))
        banner = s.recv(1024)
        return banner
    except:
        return

def main():
	if len(sys.argv) == 2:
		filename.sys.argv[1]
		if not os.path.isFile(filename):
			print 'File doesn't exist'
		if not os.access(filename, os.R_OK):
			print 'Access Denied'
			exit(0)
	else:
		print 'Usage: ' + str(sys.argv[0]) + '<vuln filename>'
		exit(0)
	portlist = 1000
	for x in range(1,255):
        ip = socket.gethostbyname(socket.gethostname()) + str(x)
		for port in range(1, portlist):
			banner = retBanner(ip.port)
			if banner:
				print ip + '/' + str(port) + ':' + banner
				checkVulns(filename, banner)
main()
			
