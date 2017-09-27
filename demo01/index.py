# -*- coding: UTF-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 4000))
print "请输入你的名字"
name = raw_input()

while True:
  print s.recv(1024)
  r = raw_input()
  s.send(name + " : " + r)
