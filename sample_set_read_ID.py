from arduino import Arduino

b = Arduino('/dev/ttyUSB0')

val = b.getID()
print ("current ID=" + val)

b.setID('11')
print ("set ID to 11")

val = b.getID()
print ("current ID=" + str(val))

