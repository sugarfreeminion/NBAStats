#! /usr/bin/env python

#Filename: StatApp.py

import sys
from StatAppGUI import *
from PyQt4.QtGui import *

def main():
    statAppGUIObj = QApplication(sys.argv)
       
    statAppGui = StatAppGUI()

    sys.exit(statAppGUIObj.exec_()) 
    
if __name__ == "__main__":
    w = main()
