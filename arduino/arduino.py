#!/usr/bin/env python

import serial

class Arduino(object):

    __OUTPUT_PINS = -1

    def __init__(self, port, baudrate=115200):
        self.serial = serial.Serial(port, baudrate)
        self.serial.write('100')

    def __str__(self):
        return "Arduino is on port %s at %d baudrate" %(self.serial.port, self.serial.baudrate)

    def output(self, pinArray):
        self.__sendData('99')
        self.__sendData(len(pinArray))

        if(isinstance(pinArray, list) or isinstance(pinArray, tuple)):
            self.__OUTPUT_PINS = pinArray
            for each_pin in pinArray:
                self.__sendData(each_pin)
        return True

    def setLow(self, pin):
        self.__sendData('0')
        self.__sendData(pin)
        return True

    def setHigh(self, pin):
        self.__sendData('1')
        self.__sendData(pin)
        return True

    def getState(self, pin):
        self.__sendData('2')
        self.__sendData(pin)
        return self.__formatPinState(self.__getData()[0])

    def analogWrite(self, pin, value):
        self.__sendData('3')
        self.__sendData(pin)
        self.__sendData(value)
        return True

    def analogRead(self, pin):
        self.__sendData('4')
        self.__sendData(pin)
        return int(self.__getData())

    def servoAdd(self, pin):
        self.__sendData('5')
        self.__sendData(pin)
        return True

    def servoWrite(self, value):
        self.__sendData('6')
        self.__sendData(str(value))
        return True

    def turnOff(self):
        for each_pin in self.__OUTPUT_PINS:
            self.setLow(each_pin)
        return True

    def getID(self):
        self.__sendData('97')
        return self.__getData()

    def setID(self, ID):
        self.__sendData('98')
        self.__sendData(ID)
        return True

    def __sendData(self, serial_data):
        while(self.__getData()[0] != "w"):
            pass
        #print("writing data: " + str(serial_data))
        self.serial.write(str(serial_data))

    def __getData(self):
        #print("reading data")
        return self.serial.readline().rstrip('\n').rstrip('\r')

    def __formatPinState(self, pinValue):
        if pinValue == '1':
            return True
        else:
            return False

    def close(self):
        self.serial.close()
        return True
