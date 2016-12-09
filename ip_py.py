#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
import netifaces

def main():
  ip = netifaces.ifaddresses('wlan0')[netifaces.AF_INET][0]['addr']
  app = QtGui.QApplication(sys.argv)
  w = QtGui.QWidget()
  w.resize(260,40)
  w.setWindowTitle("Get_IP_Address")
  w.setWindowIcon(QtGui.QIcon("pythonlogo.png"))
  label = QtGui.QLabel("wlan0:"+ip,w)
  font=QtGui.QFont()
  font.setPointSize(20)
  label.setFont(font)
  w.show()
  sys.exit(app.exec_())
  
  
  
if __name__ == "__main__":
  main()