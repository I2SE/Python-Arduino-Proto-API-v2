from arduino import Arduino
import time

b = Arduino('/dev/ttyUSB0')
#b = Arduino('COM4')
pin = 10

b.servoAdd(pin)

while 1:
    b.servoWrite(0)
    print ("set Servo to 0")
    time.sleep(3)
    b.servoWrite(90)
    print ("set Servo to 90")
    time.sleep(3)

b.close()

