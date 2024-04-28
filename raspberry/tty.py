import os
import time

usb_CH = "ttyCH"
usb_devices = []

#cheak usb devices
def GetDevList() : return os.listdir("/dev")

def GetCHDevices():
	devOld = GetDevList()

	for device in devOld:
		if usb_CH in device:
			#print (device)
			usb_devices.append("/dev/" + device)
			
	#print (usb_devices)
	return usb_devices
	
GetCHDevices()
		

