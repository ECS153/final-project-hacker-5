#!/usr/bin/python3

from socket import *
import argparse
from colored import fg

# Function to establish a connection with a given IP address and a port number
def conn_scan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        serv = getservbyport(tgtPort)
        color = fg('green')
        print(color + f'[+] port {tgtPort} is open. ' + serv)
        #print(str(serv))

    except:
        pass
        # color = fg('red')
        # print(color + f'[-] port {tgtPort} is closed.')
    finally:
        sock.close()

# Helper function that resolves DNS and calls conn_scan to scan a port
def port_scan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print(f'Unknown Host {tgtHost}')
    try:
        tgtName = gethostbyaddr(tgtIP)
        color = fg('yellow')
        print(color + f'[+] Scan Results For: ' + tgtName[0])
    except:
        color = fg('yellow')
        print(color + f'[+] Scan Results For: ' + tgtIP)

    setdefaulttimeout(2)
    for tgtPort in tgtPorts:
        conn_scan(tgtHost, tgtPort)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('host', help="Target Host")
    parser.add_argument('-p', '--ports', type=str, help="ports range\n Ex: -p 1-65535")
    args = parser.parse_args()

    tgtHost = args.host
    if args.ports == None: # scan first 1000 ports
        tgtPorts = [*range(0, 1001)]
    else: # process the input
        args.ports = str(args.ports).replace(':', '-')
        tgtPorts = str(args.ports).split('-')
        tgtPorts = [*range(int(tgtPorts[0]), int(tgtPorts[1])+1)]


    port_scan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()
