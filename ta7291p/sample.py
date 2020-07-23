import wiringpi
import time
import sys

motor1_pin = 23
motor2_pin = 24

param = sys.argv

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode( motor1_pin, 0 )
wiringpi.pinMode( motor2_pin, 0 )
print("rigth")
wiringpi.digitalWrite( motor1_pin, 1 )
wiringpi.digitalWrite( motor2_pin, 0 )
time.sleep(5)
print("stop")
wiringpi.digitalWrite( motor1_pin, 1 )
wiringpi.digitalWrite( motor2_pin, 1 )
time.sleep(5)
print("left")
wiringpi.digitalWrite( motor1_pin, 0 )
wiringpi.digitalWrite( motor2_pin, 1 )
time.sleep(5)
print("stop")
wiringpi.digitalWrite( motor1_pin, 0 )
wiringpi.digitalWrite( motor2_pin, 0 )
