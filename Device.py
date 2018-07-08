from __future__ import division
import calendar, time,random
#from SimulatedDevice import iothub_client_init,send_confirmation_callback
import os
import sys
import iothub_client
from iothub_client import IoTHubClient
import connectionModule
from connectionModule import iothub_client_init,iothub_client_telemetry_send,send_confirmation_callback


class Device():
    
    maxFlow = 200
    minFlow = 0
    maxTemprature = 50
    minTemprature = -3
    batteryLifeInSeconds = 8000000

    def __init__(self, deviceId,lon,lat,deviceType): ##Accept if fast forward is required! then put object into a mode pending number of times called.
        self.deviceId = deviceId
        self.lon = lon
        self.lat = lat
        self.deviceType = deviceType
        self.bootUpTime = calendar.timegm(time.gmtime())
        self.batteryChangeTime =  calendar.timegm(time.gmtime())
        self.batteryLifeInSeconds = 8000000
        self.base_temp = random.randrange(-5,20)
        self.connectionString = os.popen('az iot hub device-identity show-connection-string --hub-name SimTelemetry --device-id '+ self.deviceId +' --output tsv').read().rstrip()

        self.client = iothub_client_init(self.connectionString)
        #self.client = iothub_client_init('HostName=SimTelemetry.azure-devices.net;DeviceId=TFP0001;SharedAccessKey=SrK7MivXNjhqr9l04AzavMb2WP/sHCVFw2kOA80sCok=')

    def checkBattery(self):
        now = calendar.timegm(time.gmtime())
        batteryAgeInSeconds = now - self.batteryChangeTime
        batteryPercent = 100 - float(((batteryAgeInSeconds/self.batteryLifeInSeconds)*100))
        return round(batteryPercent,2)

    def changeBattery(self,newBatteryLifeInSeconds=8000000):
        self.batteryChangeTime =  calendar.timegm(time.gmtime())
        self.batteryLifeInSeconds = newBatteryLifeInSeconds

    def readPressure(self):
        pressure = random.gauss(3500,2000)
        return round(abs(pressure),3)
        #if faultTime(): ## Supposed to put the device into fault mode for a random duration of time

    def readTemprature(self):
        #Get season
        temprature = random.gauss(self.base_temp,1)
        return round(temprature,2)
        #if faultTime(): ## Supposed to put the device into fault mode for a random duration of time
    
    #def 
    def readFlow(self):
        #Get season
        flow = random.gauss(0,2000)
        return round(abs(flow),3)

    #def readHealthAlert(self):

    def faultTime(self):
        if random.randrange(1,1000,1) > 980:
            return True
        else:
            return False
        
    def sendToConnectionModule(self):
        MSG_TXT = '{\"Timestamp\":%.0f,\"DeviceId\":\"%.10s\",\"location\":{\"lon\":%.5f,\"lat\":%.5f},\"Readings\":{\"Temperature\":{\"Internal\":%.2f,\"External\":%.2f}},\"Flow\":{\"In\":%.2f,\"Out\":%.2f},\"Pressure\":%.2f,\"Battery\":%.2f}'        
        pressure = self.readPressure()
        flow = self.readFlow()
        temperature = self.readTemprature()
        battery = self.checkBattery()
        msg_txt_formatted = MSG_TXT % (calendar.timegm(time.gmtime()),self.deviceId,float(self.lat),float(self.lon),temperature,temperature*1.2, flow,flow*1.354,pressure,battery)
        #print ('DFGDFGSDFGDFGDFG ::'+self.connectionString+':::43453453453452')
        iothub_client_telemetry_send(self.client,msg_txt_formatted[:])