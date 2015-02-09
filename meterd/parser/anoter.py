''' Module  '''

import re
import logging


class Another:
    ''' Class '''

    def __init__(self, data=None, logger=None):
        ''' Method '''
        self._data = data
        self.logger = logger or logging.getLogger(__name__)
        self.time = None
        self.uid = None
        self.value = None

    def parse_data(self):
        ''' Method '''

        try:
            '''#http://www.marcus-povey.co.uk - USED REGEX REGEX!'''
            uidregex = re.compile('<id>([0-9]+)</id>')
            valueregex = re.compile('<watts>([0-9]+)</watts>')
            timeregex = re.compile('<time>([0-9\.\:]+)</time>')
            self.value = str(int(valueregex.findall(self._data)[0]))
            self.time = timeregex.findall(self._data)[0]
            self.uid = uidregex.findall(self._data)[0]
            self.logger.info('Parsed data sucessfully!')

        except Exception:
            self.logger.error('Could not get details from device',
                              exc_info=True)
