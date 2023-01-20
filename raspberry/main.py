import time

from irsensor import IRSensor
from lcd1602 import LCD1602
from dhtsensor import DHTsensor
import RPi.GPIO as GPIO

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    irsensor = IRSensor()
    dhtsensor = DHTsensor()
    lcd1602 = LCD1602()
    oldtime = time.time()
    try:
        lcd1602.start()
        dhtsensor.check_sensor()
        while True:
            irsensor.check_sensor()
            if time.time() - oldtime > 300:
                dhtsensor.check_sensor()
                oldtime = time.time()
            lcd1602.show_on_screen()
            time.sleep(5)

    except KeyboardInterrupt:
        pass

    finally:
        lcd1602.close()
        GPIO.cleanup()
