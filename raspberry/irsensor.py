import RPi.GPIO as GPIO


class IRSensor:

    def check_sensor(self):
        sensor = 17

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(sensor, GPIO.IN)

        if not GPIO.input(sensor):
            print("found object")


