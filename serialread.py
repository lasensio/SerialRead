import serial
comunicacaoSerial = serial.Serial('/dev/cu.usbserial-AH03AYMB',9600)

while 1 :
    print comunicacaoSerial.readline()
