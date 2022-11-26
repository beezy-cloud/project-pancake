# Copyright 2022 Rom Adams (https://github.com/romdalf) at Red Hat Inc. 
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import machine
from machine import Pin
import time 
import network
import socket
import utime

## NFC reader ############################################################
# import NFC reader library
from mfrc522 import MFRC522

# connecting to network 
reader = MFRC522(spi_id=0,sck=2,miso=4,mosi=3,cs=1,rst=0)
previousCard = [0]

def cardReader():
    while True: 
        reader.init()
        (stat, tag_type) = reader.request(reader.REQIDL)
        if uid == previousCard:
            continue
        if stat == reader.OK:
            (stat, uid) = reader.SelectTagSN()
            if stat == reader.OK:
                print("Card detected {}  uid={}".format(hex(int.from_bytes(bytes(uid),"little",False)).upper(),reader.tohexstring(uid)))
                defaultKey = [255,255,255,255,255,255]
                reader.MFRC522_DumpClassic1K(uid, Start=0, End=64, keyA=defaultKey)
                print("Done")
                previousCard = uid
            else:
                pass
        else:
            previousCard = [0]
        utime.sleep_ms(50) 

## motor setup ###########################################################
# defined used pins on the board
motorOneFW = Pin(18, Pin.OUT)
motorOneBW = Pin(19, Pin.OUT)
motorTwoFW = Pin(20, Pin.OUT)
motorTwoBW = Pin(21, Pin.OUT)

# define movements 
def moveForward():
    motorOneFW.value(1)
    motorTwoFW.value(1)
    motorOneBW.value(0)
    motorTwoBW.value(0)

def moveBackward():
    motorOneFW.value(0)
    motorTwoFW.value(0)
    motorOneBW.value(1)
    motorTwoBW.value(1)

def moveRight():
    motorOneFW.value(0)
    motorTwoFW.value(1)
    motorOneBW.value(1)
    motorTwoBW.value(0)

def moveLeft():
    motorOneFW.value(1)
    motorTwoFW.value(0)
    motorOneBW.value(0)
    motorTwoBW.value(1)

def moveStop():
    motorOneFW.value(0)
    motorTwoFW.value(0)
    motorOneBW.value(0)
    motorTwoBW.value(0)

# default state is fullstop 
moveStop()

## network connection ####################################################

# SSID with credentials for wireless connection 
networkName = 'NCC-1031-A'
networkPassword= 'prouteprouteproute!'

# connecting to network 
def connecting():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(networkName, networkPassword)
        while not wlan.isconnected():
            print('waiting for connection...')
            pass 
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip 


# create a network socket
def networkSocket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection 

def webControl():
    html = f"""
            <!DOCTYPE html>
            <html>
            <head>
            <title>Zumo Robot Control</title>
            </head>
            <center><b>
            <form action="./forward">
            <input type="submit" value="Forward" style="height:120px; width:120px" />
            </form>
            <table><tr>
            <td><form action="./left">
            <input type="submit" value="Left" style="height:120px; width:120px" />
            </form></td>
            <td><form action="./stop">
            <input type="submit" value="Stop" style="height:120px; width:120px" />
            </form></td>
            <td><form action="./right">
            <input type="submit" value="Right" style="height:120px; width:120px" />
            </form></td>
            </tr></table>
            <form action="./backward">
            <input type="submit" value="Back" style="height:120px; width:120px" />
            </form>
            </body>
            </html>
            """
    return str(html)

def webServer(connection):
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/forward?':
            moveForward()
        elif request == '/backward?':
            moveBackward()
        elif request == '/right?':
            moveRight()
        elif request == '/left?':
            moveLeft()
        elif request == '/stop?':
            moveStop()
        html = webControl()
        client.send(html)
        client.close()

try:
    cardReader()
    ip = connecting()
    connection = networkSocket(ip)
    webServer(connection)
except KeyboardInterrupt:
    machine.reset()
