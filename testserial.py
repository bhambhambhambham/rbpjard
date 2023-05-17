import serial

ser = serial.Serial('/dev/ttyACM0', 9600)
i = 0
while i >= 0 :
    data = ser.readline()
    string = data.decode().strip()
    print(string)

    
    