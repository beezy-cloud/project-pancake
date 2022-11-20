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
import time 
import network
import socket

## wireless network connection 

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
    print('network config: ', wlan.ifconfig())

