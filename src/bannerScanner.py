#!/usr/bin/python
import socket
import os
import sys
filename = "banners.txt"
def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip.port))
        banner = s.recv(1024)
        return banner
    except:
        return

def checkVulns(filename,banner):
    f = open(filename, "r")
    for line in f.readLines():
        if line.strip("\n") in banner:
            print "server is vulnerable: " + banner.strip("\n")

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print 'File doesnt exist'
                exit(0)
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
			banner = retBanner(ip,port)
			if banner:
				print ip + '/' + str(port) + ':' + banner
				checkVulns(filename, banner)
main()
			
