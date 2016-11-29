#!/usr/bin/python
#-*- coding: utf-8 -*-

import socket
import netifaces

print socket.gethostbyname(socket.gethostname())
print netifaces.ifaddresses('wlan0')[netifaces.AF_INET][0]['addr']
