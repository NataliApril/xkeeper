import os

os.system("cd ")
#search esp
#s = os.system("esptool.py --port /dev/ttyUSB0 --chip auto chip_id")

#load *.bin file
s = os.system("esptool.py --chip esp8266 --baud 115200 --port /dev/ttyUSB0 write_flash -z 0x0 /home/user/xkeeper/sketch_may06a/sketch_may06a.ino.esp8285.bin")
if s == 0:
	print ("sucess")
else:
	print ("error = ", s)
