import os
import time

usb_CH = "ttyCH"
usb_devices = []

#cheak usb devices
def GetDevList() : return os.listdir("/dev")

def GetCHDevices(_str):
	devOld = GetDevList()
	for device in devOld:
		if _str in device:
			usb_devices.append("/dev/" + device)
	return usb_devices
	
		

