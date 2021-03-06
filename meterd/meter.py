#!/usr/bin/python
import sys
import serial
import re
import time
import logging
from reading import Reading


class Meter(object):

    class MeterReadngException(Exception):
        def __init__(self, msg):
            self.msg = msg

        def __str__(self):
            return self.msg

    '''Constructors'''
    def __init__(self, port='/dev/ttyUSB0', baud=57600,
                 timeout=10, uid=None, unit='w', logger=None):
        '''Public Vars'''
        self.port = port
        self.baud = baud
        self.timeout = timeout
        self.uid = uid
        self.unit = unit
        self.logger = logger or logging.getLogger(__name__)
        '''Prvate Vars'''
        self._r = None
        self._data = None
        #self._meter = None
        self._meter = serial.Serial(self.port, self.baud, timeout=self.timeout)

    '''Properties (Getters/Setters'''
    '''? @property decorator?'''
    '''
    def set_email(self, value)
        if '@' not in value:
            raise Exception("This doesn't look like an email address.")
        self._email = value

    def get_email(self):
        return self._email

    email = property(get_email, set_email)
    '''

    '''Methods'''
    def __str__(self):
        return "Meter: " + self.uid

    def open(self):
        self._meter.open()

    def read(self):
        try:
            self._data = self._meter.readline()

        except:
            pass

    def close(self):
        self._meter.close()
    
    def parse(self):
        try:
            #http://www.marcus-povey.co.uk - USED REGEX REGEX!
            uidRegex = re.compile('<id>([0-9]+)</id>')
            valueRegex = re.compile('<watts>([0-9]+)</watts>')
            timeRegex = re.compile('<time>([0-9\.\:]+)</time>')
            value = str(int(valueRegex.findall(self._data)[0]))
            time = timeRegex.findall(self._data)[0]
            self.uid = uidRegex.findall(self._data)[0]
            self.logger.info('Parsed data sucessfully!')
            self._r = Reading(self, value, time, self.logger)

        except Exception:
            self.logger.error('Could not get details from device')
    
    def submit(self):
        try:
            self._r.submit()
        except Exception:
            self.logger.error('Reading not initialised')
        self._r = None
