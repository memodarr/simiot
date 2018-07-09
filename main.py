from Device import Device
import csv
import time
def createDevice(deviceCount):
    devices=[]

    with open('locs.csv', 'rb') as f:
    	reader = csv.reader(f)
    	locs = list(reader)

    for i in range(0,deviceCount):
        device = Device('TFP'+str(i+1).zfill(4) ,locs[i][0],locs[i][1],'Generic Sensor')
        devices.append(device)
    return devices


if __name__ == '__main__':
    print ( "IoT Hub Quickstart #1 - Simulated device" )
    print ( "Press Ctrl-C to exit" )
    devices = createDevice(1)

    while True:
        for device in devices:
            device.sendToConnectionModule()
        time.sleep(3)
    
