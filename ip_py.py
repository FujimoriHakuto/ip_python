#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

import socket

def main():
  app = QtGui.QApplication(sys.argv)
  w = QtGui.QWidget()
  w.resize(300,50)
  w.setWindowTitle("Get_IP_Address")
  w.setWindowIcon(QtGui.QIcon("pythonlogo.png"))
  w.show()
  sys.exit(app.exec_())
  
  
  
if __name__ == "__main__":
  main()