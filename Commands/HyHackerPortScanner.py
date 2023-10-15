#!/bin/python3

import sys 
import socket 
from datetime import datetime

if len(sys.argv)==2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments")
    print("Syntax: python3 HyHackerPortScanner.py <ip>")

print("-"*50)
print("Scanning target "+str(sys.argv[1]+" whose Ip is "+str(target)))
print("Time started: "+str(datetime.now()))    
print("-"*50)

try: 
    for port in range(1,100):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"Port {port} is open")
            s.close()
        else:
            print(f"Port {port} is closed")
            s.close()
except KeyboardInterrupt:
    print("\nExisting program.")
    sys.exit()

except socket.gaierror:
    print("\nHostname could not be resolved ")
    sys.exit()

except socket.error:
    print("\nCould not connect to the server ")
    sys.exit()
