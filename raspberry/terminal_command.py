import os

os.system("cd")
os.system("esptool.py --port /dev/ttyUSB0 --chip auto read_mac")
