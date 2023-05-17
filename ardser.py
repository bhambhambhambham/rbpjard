import serial
import time

screen = serial.Serial('', 9600)

def write(x):
    screen.write(bytes(x, 'utf-8'))
    time.sleep(0.1)
    return

write(1) ## fat / white
write(2) ## fat / green
write(3) ## fat / red
write(4) ## protein / white
write(5) ## protein / yellow
write(6) ## protein / green
write(7) ## protein / red
write(8) ## vitamin / white
write(9) ## vitamin / yellow
write(10) ## vitamin / yellowgreen
write(11) ## vitamin / green
write(12) ## vitamin / red
write(13) ## carbohydrate / white
write(14) ## carbohydrate / bright yellow
write(15) ## carbohydrate / yellow
write(16) ## carbohydrate / yellow green
write(17) ## carbohydrate / green
write(18) ## carbohydrate / red
write(19) ## restart (every portion = white)