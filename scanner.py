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
	portlist = [21,22,25,80,110,443,445]
	for x in range(4,6):
		ip = '192.168.1.' + str(x)
		for port in portlist:
			banner = retBanner(ip.port)
			if banner:
				print ip + '/' + str(port) + ':' + banner
				checkVulns(filename, banner)
main()
			
