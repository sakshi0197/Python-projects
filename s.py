#!/usr/bin/python2

import socket,time
sen_ip="127.0.0.1"
my_port=9999
#                     ipv4        UDP
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#now sending data to other side

s.sendto("hii",("127.0.0.1",8888))

