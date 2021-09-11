#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from datetime import datetime  as dt
import logging
import json

import sys


from particle_counter import ParticleCounter
# Make instance
device001 = ParticleCounter(30)

# Set signal pin
device001.set_pin_number(PIN=14)

# Excute
device001.particle_count(count_times=1000000)

# Finish
GPIO.cleanup()
print('==== Done ====')