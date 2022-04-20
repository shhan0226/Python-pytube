import serial
import time

sec = 60 * 1

print("start...")
print("Voltage(Vo), Ampere(Am), Wattage(Wa), Watt hours(Wh), Power Factor(pf), Hertz(Hz)")

# serial connection
SerialObj = serial.Serial('/dev/ttyUSB0', 9600)
#print('\nStatus -> ', SerialObj)

# time stemp
max_time_end = time.time() + (sec)

# serial write - start
BytesWritten = SerialObj.write(b'E#')
BytesWritten = SerialObj.write(b'S#')
#print(BytesWritten)

#time.sleep(1)

# serial read
while True:
    ReceivedString = SerialObj.readline()
    #print (ReceivedString)
    print (ReceivedString.decode().strip())
    if time.time() > max_time_end:
        break

# serial write - end
BytesWritten = SerialObj.write(b'E#')
#print(BytesWritten)

# serial exit
SerialObj.close()

