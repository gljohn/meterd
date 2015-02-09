#!/usr/bin/python
import weakref
import logging


class Reading(object):

    def __init__(self, parent, value=None, timestamp=None, logger=None):
        self.parent = weakref.ref(parent)
        self.value = value
        self.timestamp = timestamp
        self.unit = parent.unit
        self.uid = parent.uid
        self.logger = logger or logging.getLogger(__name__)

    def __str__(self):
        return ("value=" + str(self.value) + "&"
                + "time=" + str(self.timestamp) + "&"
                + "unit=" + str(self.unit) + "&"
                + "meterid=" + str(self.uid))

    def submit(self):
        #DO HTTP SEND HERE.
        self.logger.info(self)
