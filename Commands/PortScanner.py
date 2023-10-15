#!/bin/python3 
import socket 
import sys
from datetime import datetime
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)
if len(sys.argv)==2:
    TargetIp = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments")
    print("Syntax: python3 PortScanner.py <ip>")

print("_"*50)
print("Hydot Hacker Diary POrt Scaning ")
print("Scanning target "+str(sys.argv[1]+" whose Ip is "+str(TargetIp)))
print("Time started: "+str(datetime.now()))    
print("_"*50)


for Port in range(1,1000):
    try:
    
       s.connect((TargetIp,Port))

       print("Port "+str(Port)+" is Open")

    except KeyboardInterrupt:
        print("\nExisting program.")
        sys.exit()

    except socket.gaierror:
        print("\nHostname could not be resolved ")
        sys.exit()

    except socket.error:
        print("Port "+str(Port)+" is Closed")
      

