"""
Created on Apr 4, 2014
Updated on May 31, 2017

@author: Dario Bonino
@author: Luigi De Russis

Copyright (c) 2014-2017 Dario Bonino and Luigi De Russis

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License
"""

import rest
import time


if __name__ == '__main__':

    # the base url
    base_url = 'http://192.168.0.202:8083'

    # login credentials, to be replaced with the right ones
    # N.B. authentication may be disabled from the configuration of the 'Z-Wave Network Access' app
    # from the website available at 'base_url'
    username = "admin"
    password = "password"

    # get z-wave devices
    all_devices = rest.send(url=base_url+'/ZWaveAPI/Data/0', auth=(username, password))
    # without auth, omit the last parameter
    # all_devices = rest.send(url=base_url+'/ZWaveAPI/Data/0')

    # search switches
    for device_key in all_devices['devices']:
        # iterate over device instances
        for instance in all_devices['devices'][device_key]['instances']:
            # search for the 37 (SwitchBinary) command class
            if '37' in all_devices['devices'][device_key]['instances'][instance]['commandClasses'].keys():
                # debug
                print("device %s is a switch" % device_key)
                # turn it on
                url_to_call = base_url+"/ZWaveAPI/run/devices["+device_key+"].instances["+instance+"].commandClasses[37].Set(255)"
                rest.send(url=url_to_call, auth=(username, password))

    # reverse count to off
    for i in range(0, 10):
        time.sleep(1)
        print(10-i)

    # search switches
    for device_key in all_devices['devices'].keys():
        # iterate over device instances
        for instance in all_devices['devices'][device_key]['instances']:
            # search for the 37 (SwitchBinary) command class
            if '37' in all_devices['devices'][device_key]['instances'][instance]['commandClasses'].keys():
                # debug
                print("device %s is a switch" % device_key)
                # turn it off
                url_to_call = base_url+"/ZWaveAPI/run/devices["+device_key+"].instances["+instance+"].commandClasses[37].Set(0)"
                rest.send(url=url_to_call, auth=(username, password))
