# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_dht
import requests
from lcd1602 import LCD1602

class DHTsensor:

    public_ip = ""

    def __init__(self):
        self.dhtDevice = adafruit_dht.DHT22(board.D4)

    def check_sensor(self):

        try:
            # Print the values to the serial port
            temperature_c = self.dhtDevice.temperature
            humidity = self.dhtDevice.humidity
            data = {"temperature": temperature_c,
                    "humidity": humidity
                    }
            response = requests.post('http://' + self.public_ip + ':5000/api/addsensordata',
                                     timeout=5, verify=False, json=data)
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(2.0)
        except requests.exceptions.Timeout:
            print("Timeout error")
            LCD1602().timeout()
        except Exception as e:
            print(e)
            LCD1602().timeout()    
