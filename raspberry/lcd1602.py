# SPDX-FileCopyrightText: 2018 Mikey Sklar for Adafruit Industries
#
# SPDX-License-Identifier: MIT

from subprocess import Popen, PIPE
from time import sleep
from datetime import datetime
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
import requests


class LCD1602:
    lcd_columns = 16
    lcd_rows = 2

    lcd_rs = digitalio.DigitalInOut(board.D7)
    lcd_en = digitalio.DigitalInOut(board.D8)
    lcd_d4 = digitalio.DigitalInOut(board.D25)
    lcd_d5 = digitalio.DigitalInOut(board.D24)
    lcd_d6 = digitalio.DigitalInOut(board.D23)
    lcd_d7 = digitalio.DigitalInOut(board.D18)

    # Initialise the lcd class
    lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6,
                                          lcd_d7, lcd_columns, lcd_rows)

    def show_on_screen(self):
        try:

            response = requests.get('http://192.168.1.181:5000/api/getlastsensordata', timeout=5).json()
            humidities = response["humidities"]
            temperatures = response["temperatures"]
            if len(humidities) > 0 and len(temperatures) > 0:
                self.lcd.clear()
                temperature_avg = sum(temperatures) / len(temperatures)
                humidity_avg = sum(humidities) / len(humidities)
                lcd_line_1 = "Temperat: " + str(temperature_avg)[:5] + "\n"
                lcd_line_2 = "Humidity: " + str(humidity_avg)[:5] + "%"
                self.lcd.message = lcd_line_1 + lcd_line_2
            elif len(response["ids"]) == 0:
                self.calibrate()
        except requests.exceptions.Timeout:
            self.timeout()
        except requests.exceptions:
            self.timeout()

    def start(self):
        self.lcd.clear()
        lcd_line_1 = "Starting...\n"
        lcd_line_2 = ""
        self.lcd.message = lcd_line_1 + lcd_line_2

    def timeout(self):
        self.lcd.clear()
        lcd_line_1 = "API IS OFFLINE\n"
        lcd_line_2 = "Retrying..."
        self.lcd.message = lcd_line_1 + lcd_line_2

    def calibrate(self):
        self.lcd.clear()
        lcd_line_1 = "Calibrating...\n"
        lcd_line_2 = ""
        self.lcd.message = lcd_line_1 + lcd_line_2

    def close(self):
        self.lcd.clear()
        lcd_line_1 = "Raspberry Pi\n"
        lcd_line_2 = "is idling..."

        # combine both lines into one update to the display
        self.lcd.message = lcd_line_1 + lcd_line_2
