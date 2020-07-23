import wiringpi
import time
import sys

motor_pin_1 = 23
motor_pin_2 = 24

wiringpi.wiringPiSetupGpio() #initilize GPIO control

print("stop 5sec")
wiringpi.pinMode( motor_pin_1, 0 )
wiringpi.pinMode( motor_pin_2, 0 )
print("right 5sec")
wiringpi.digitalWrite( motor_pin_1, 1 )
wiringpi.digitalWrite( motor_pin_2, 0 )
time.sleep(5)
print("stop 5sec")
wiringpi.digitalWrite( motor_pin_1, 1 )
wiringpi.digitalWrite( motor_pin_2, 1 )
time.sleep(5)
print("left 5sec")
wiringpi.digitalWrite( motor_pin_1, 0 )
wiringpi.digitalWrite( motor_pin_2, 1 )
time.sleep(5)
print("stop 5sec")
wiringpi.digitalWrite( motor_pin_1, 0 )
wiringpi.digitalWrite( motor_pin_2, 0 )
print("Done")