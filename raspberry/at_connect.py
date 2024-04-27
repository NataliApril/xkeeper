import serial

serial_port = serial.Serial('COM1', '9600')

command = "AT\r\n"

serial_port.write(command.encode())
response = serial_port.read_all().decode()
print (response)
