# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import random
import calendar
import time
import sys
import csv

# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
import iothub_client
# pylint: disable=E0611
from iothub_client import IoTHubClient, IoTHubClientError, IoTHubTransportProvider, IoTHubClientResult
from iothub_client import IoTHubMessage, IoTHubMessageDispositionResult, IoTHubError, DeviceMethodReturnValue

# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table
#CONNECTION_STRING = "HostName=SimTelemetry.azure-devices.net;DeviceId=TFP0001;SharedAccessKey=SrK7MivXNjhqr9l04AzavMb2WP/sHCVFw2kOA80sCok="

# Using the MQTT protocol.
PROTOCOL = IoTHubTransportProvider.MQTT
MESSAGE_TIMEOUT = 10000

# Define the JSON message to send to IoT Hub.
#MSG_TXT = '{\"Timestamp\":%.0f,\"DeviceId\":\"%.10s\",\"location\":{\"lon\":%.5f,\"lat\":%.5f},\"Readings\":{\"Temperature\":{\"Internal\":%.2f,\"External\":%.2f}},\"Flow\":{\"In\":%.2f,\"Out\":%.2f},\"Pressure\":%.2f,\"Battery\":%.2f}'

def send_confirmation_callback(message, result, user_context):
    print ( "IoT Hub responded to message with status: %s" % (result) )

def iothub_client_init(CONNECTION_STRING):
    # Create an IoT Hub client
    client = IoTHubClient(CONNECTION_STRING, PROTOCOL)
    return client



