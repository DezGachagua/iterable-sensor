"""  Iterator for Streamed Sensor Data.
I combined it with a timestamp generator and created a small system for logging sensor data every 
second. """

import datetime
import itertools
import random
import time

# This class mimics a sensor and produces a stream of  data


class Sensor:

    # this method an iterator which is the same object
    def __iter__(self):
        return self

# this method simply returns a random number but imagine a more complex code that actually...
# ... read real values from a sensor
    def __next__(self):
        return random.random()


sensor = Sensor()
timestamps = iter(datetime.datetime.now,  None)

for stamp,  value in itertools.islice(zip(timestamps,  sensor),  10):
    print(stamp,  value)
    time.sleep(1)
