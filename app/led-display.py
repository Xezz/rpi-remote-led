# coding=utf-8
import logging
import sys
from app.RPi import GPIO

__author__ = 'Xezz'
__version__ = '0.1'
__test__ = True


def main():
    value_to_led = [11, 13, 15, 17]
    display = LedDisplay(value_to_led)
    GPIO.setmode(GPIO.BCM)

    compare = raw_input('> ')
    try:
        compare = int(compare)
        display.lightLEDs(compare)
    except ValueError as e:
        print e.message
        GPIO.cleanup()
        sys.exit(1)


class LedDisplay(object):
    def __init__(self, LEDs):
        super(LedDisplay, self).__init__()
        self.leds = {}
        # fill the dict with the values of the list
        # the keys are 2**x aka 1,2,4....
        if isinstance(LEDs, list):
            for x in range(len(LEDs)):
                self.leds[2**x] = LEDs[x]
        self.max_value = 2**len(LEDs) - 1
        self.initializePins()

    def initializePins(self):
        GPIO.setmode(GPIO.BCM)
        for v in self.leds.itervalues():
            GPIO.setup(v, GPIO.OUT)

    def lightLEDs(self, *args):
        for num in args:
            if isinstance(num, int) and 0 <= num:
                if num <= self.max_value:
                    logging.warn('Input is bigger than possible. max{} / input {}'.format(self.max_value, num))
                for k, v in self.leds.iteritems():
                    GPIO.output(v, num & k > 0)

if __name__ == "__main__":
    # FIXME: Logger not working yet
    GPIO.debug = __test__
    main()