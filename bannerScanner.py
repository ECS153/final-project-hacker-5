#!/usr/bin/python
import socket
import os
import sys

def checkVulns(filename,banner):
    f = open(filename, "r")
    for line in f.readLines():
        if line.strip("\n") in banner:
            print "server is vulnerable: " + banner.strip("\n")

def retBanner(ip,port):
    try:
	print "h"
        socket.setdefaulttimeout(2)
	print "d"
        s = socket.socket()
	print ip
	print port
        s.connect((ip,port))
	print "dwe"
        banner = s.recv(1024)
	print banner
        return banner
    except:
	print "oh no"
        return

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print 'File doesnt exist'
		if not os.access(filename, os.R_OK):
			print 'Access Denied'
			exit(0)
	else:
		print 'Usage: ' + str(sys.argv[0]) + '<vuln filename>'
		exit(0)
	portlist = 22
	for x in range(0,10):
    		ip0 = socket.gethostbyname(socket.gethostname()).split(".")[0] + "."
		ip1 = ip0 + socket.gethostbyname(socket.gethostname()).split(".")[1] + "."
		ip2 = ip1 + socket.gethostbyname(socket.gethostname()).split(".")[2] + "."
		ip = ip2 + str(x)
		print ip
		for port in range(1, portlist):
			print str(ip) + " and " + str(port)
			banner = retBanner(ip,port)
			if banner:
				print ip + '/' + str(port) + ':' + banner
				checkVulns(filename, banner)
main()		
