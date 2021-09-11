import RPi.GPIO as GPIO
import time
from datetime import datetime  as dt
import logging
import json
import sys

import logging
logger = logging.getLogger(__name__)

fmt = "[%(asctime)s][%(levelname)s] %(name)s :%(message)s"
logging.basicConfig(level=logging.DEBUG, format=fmt)

class ParticleCounter():

    def __init__(self,sampling_sec):
        self.sampling_sec = 30
        pass

    def set_pin_number(self, PIN=21):
        self.PIN = PIN
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PIN, GPIO.IN)
        GPIO.setwarnings(False)
                
    def particle_count(self, count_times=10):
        self.count_times = count_times
        logging.info("Start")
        for i in range(self.count_times):
            logging.info("Rev:{0}".format(i))
            low_pulse_time_rst = self.get_low_pulse_time()
            concentration_rst = self.get_concentration(low_pulse_time_rst['during_low'],low_pulse_time_rst['t_end'])
            low_pulse_time_rst.update(concentration_rst)
            logger.info(" Rst:{0}".format(low_pulse_time_rst['concentration']))
            self.write_data(low_pulse_time_rst)
            
    def get_low_pulse_time(self):
        t_start = time.time()
        during_low,t_current = 0,0
        while True:
            during_low += self.time_low()
            t_current = (time.time() - t_start)
            if (t_current  > self.sampling_sec):
                break
        return {'during_low':during_low, 't_start':t_start, 't_end':t_current}
    
    def get_concentration(self,during_low_sec, sampling_sec):
        ratio = 100*during_low_sec/sampling_sec;
        concentration = 1.1*pow(ratio,3)-3.8*pow(ratio,2)+520*ratio+0.62        
        return {'ratio':ratio, 'concentration':concentration}
    
    def write_data(self,dict_obj):
        dict_obj['write_time'] = dt.now().strftime("%Y%m%d%H%M%s%Z")
        with open('file.txt', 'a') as file:
            file.write(json.dumps(dict_obj))
            file.write(',\n')


    def time_low(self):     
        t_start = time.time()
        t_end = time.time()

        if GPIO.input(self.PIN) == 1:
            return 0.0
        
        while GPIO.input(self.PIN) == 0:
            t_end = time.time()

        return (t_end - t_start)
