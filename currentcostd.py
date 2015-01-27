#!/usr/bin/python
##################################################
# currentcostd.py                                #
#                                                #
# @author Gareth John <gljohn@fedoraproject.org> #
##################################################


import sys, time, logging, logging.handlers
from daemon import Daemon
from meter import Meter
class MeterDaemon(Daemon):
        def __init__(self, pid):
                self.logger = logging.getLogger(__name__)
                self.logger.setLevel(logging.INFO)
                ##create a file handler
                handler = logging.FileHandler('/var/log/hello.log')
                handler.setLevel(logging.INFO)
                ##create a logging format
                formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
                handler.setFormatter(formatter)
                ##add the handlers to the logger
                self.logger.addHandler(handler)
                self.logger.info('Logging started...')
                self.logger.info('Pid is:' + pid)
                super(MeterDaemon, self).__init__(pid)
                #self.m = Meter('/dev/ttyUSB0', 57600, 8, 'mastermeter', 'watts', self.logger)
                
        def run(self):
                self.m = Meter('/dev/ttyUSB0', 57600, 8, 'mastermeter', 'watts', self.logger)
                self.m.open()
                self.logger.debug('Meter open.')
                while 1:
                        self.m.open()
                        self.m.read()
                        self.m.parse()
                        self.m.submit()
                        time.sleep(6)

        def stop(self):
                #self.m.close()
                self.logger.debug('Meter close.')
                super(MeterDaemon, self).stop()
                        
                        
if __name__ == "__main__":
        daemon = MeterDaemon('/tmp/meter-daemon.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)
        else:
                print "usage: %s start|stop|restart" % sys.argv[0]
                sys.exit(2)
