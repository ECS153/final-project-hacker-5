#!/usr/bin/python
import socket
import os
import sys

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
    except socket.error, exc:
        print "Caught exception socket.error : %s" % exc
        return


def checkVulns(filename,banner):
    f = open(filename, "r")
    for line in f.readLines():
        if line.strip("\n") in banner:
            print "server is vulnerable: " + banner.strip("\n")

def main():
    portstart = 219
    portfinish = 220
    for x in range(0,255):
            ip0 = socket.gethostbyname(socket.gethostname()).split(".")[0] + "."
            ip1 = ip0 + socket.gethostbyname(socket.gethostname()).split(".")[1] + "."
            ip2 = ip1 + socket.gethostbyname(socket.gethostname()).split(".")[2] + "."
            ip = ip2 + str(x)
            for port in range(portstart, portfinish):
                print str(ip) + " and " + str(port)
                banner = retBanner(ip,port)
                if banner:
                    print ip + '/' + str(port) + ':' + banner
                    checkVulns(filename, banner)
main()
