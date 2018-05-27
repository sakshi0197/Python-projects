#!/usr/bin/python2

import socket

rec_ip="127.0.0.1"
my_port=8888

x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
x.bind((rec_ip,my_port))

d=x.recvfrom(1000)
print (d)
