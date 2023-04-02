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

import utime 
import ujson
import network
import ubinascii
import machine
from machine import Pin
import socket

# getting a ISO8601 timestamp format
def timestamp():
    current_time = utime.localtime()
    time = '{:04d}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}Z'.format(
        current_time[0], current_time[1], current_time[2],
        current_time[3], current_time[4], current_time[5])
    return time

# print device and software info
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
print(f"{timestamp()} - WRCR: {mac} v0.1 DEV RELEASE")

# network connection ####################################################
networkName = 'Proximus-Home-3A80'
networkPassword= 'weeawf677xh9e'

# connecting to network 
def connecting():
    if not wlan.isconnected():
        print(f"{timestamp()} - WLAN connecting to network...")
        wlan.connect(networkName, networkPassword)
        print(f"{timestamp()} - WLAN waiting for connection...")
        while not wlan.isconnected():
            pass 
    ip = wlan.ifconfig()[0]
    print(f"{timestamp()} - WLAN connected on {networkName} with IP {ip}")
    return ip

# motor setup
motorOneFW = Pin(18, Pin.OUT)
motorOneBW = Pin(19, Pin.OUT)
motorTwoFW = Pin(20, Pin.OUT)
motorTwoBW = Pin(21, Pin.OUT)

# define movements
def moveStop():
    motorOneFW.value(0)
    motorOneBW.value(0)
    motorTwoFW.value(0)
    motorTwoBW.value(0)

def moveForward():
    motorOneFW.value(1)
    motorOneBW.value(1)
    motorTwoFW.value(0)
    motorTwoBW.value(0)
    utime.sleep(1)
    moveStop()

def moveBackward():
    motorOneFW.value(0)
    motorOneBW.value(0)
    motorTwoFW.value(1)
    motorTwoBW.value(1)
    utime.sleep(1)
    moveStop()

def moveLeft():
    motorOneFW.value(1)
    motorOneBW.value(0)
    motorTwoFW.value(0)
    motorTwoBW.value(1)
    utime.sleep(1)
    moveStop()

def moveRight():
    motorOneFW.value(0)
    motorOneBW.value(1)
    motorTwoFW.value(1)
    motorTwoBW.value(0)
    utime.sleep(1)
    moveStop()

# create a network socket
socketPort = 80
def networkSocket(ip):
    address = (ip, socketPort)
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print(f"{timestamp()} - Try to start a Network Socket...")
        connection.bind(address)
    except OSError:
        old = connection.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
        print(f"{timestamp()} - Socket state {old} already in use!")
        connection.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
        new = connection.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
        print(f"{timestamp()} -Socket state {new}")
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.bind(address)
    print(f"{timestamp()} - Socket started on {ip} on port {socketPort}")
    connection.listen(1)
    return connection

def webControl():
    html = f"""
            <!DOCTYPE html>
            <html>
            <head>
            <title>WRCR</title>
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
    print(f"{timestamp()} - webServer started with webControl as Index")
    while True:
        status = Pin("LED", Pin.OUT)
        status.toggle()
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            print(f"{timestamp()} - webServer failed due to IndexError!")
            pass
        if request == '/forward?':
            print(f"{timestamp()} - webControl called for moveForward")
            moveForward()
        elif request == '/backward?':
            print(f"{timestamp()} - webControl called for moveBackward")
            moveBackward()
        elif request == '/right?':
            print(f"{timestamp()} - webControl called for moveRight")
            moveRight()
        elif request == '/left?':
            print(f"{timestamp()} - webControl called for moveLeft")
            moveLeft()
        elif request == '/stop?':
            print(f"{timestamp()} - webControl called for moveStop")
            moveStop()
        html = webControl()
        client.send(html)
        client.close()

try:
    ip = connecting()
    connection = networkSocket(ip)
    webServer(connection)
except KeyboardInterrupt:
    machine.reset()
